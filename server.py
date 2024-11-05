import grpc
from concurrent import futures
import auth_pb2
import auth_pb2_grpc
import hashlib
import psycopg2
from psycopg2 import sql
import requests
import jwt
import time


# Configurações JWT
SECRET_KEY = "CurvoAndCarlosKey"  # Chave secreta para assinar os tokens JWT
TOKEN_EXPIRATION = 120  # Expiração do token em segundos (2 min)

# Função para criar um token JWT
def generate_token(email):
    payload = {
        "email": email,
        "exp": time.time() + TOKEN_EXPIRATION  # Define o tempo de expiração
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Função para verificar e decodificar o token JWT
def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True, None
    except jwt.ExpiredSignatureError:
        return False, "Token expirado"
    except jwt.InvalidTokenError:
        return False, "Token inválido"

# Configurações do banco de dados
db_config = {
    'dbname': 'wlfkmzop',
    'user': 'wlfkmzop',
    'password': '7Dl6j_Q0h5Q-Z5sqXH_o8TreI3sMngIT',
    'host': 'isabelle.db.elephantsql.com',
    'port': '5432',
}

# Conectar ao banco de dados
def get_db_connection():
    return psycopg2.connect(**db_config)

class AuthService(auth_pb2_grpc.AuthServiceServicer):

    def Register(self, request, context):
        email = request.email
        password_hash = hashlib.sha256(request.password.encode()).hexdigest()

        resposta = verificar_email(email)
        if resposta.get("status") == "invalid":
            return auth_pb2.AuthResponse(success=False, message=f"Erro: Email não é válido.")
        
        
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Verificar se o usuário já existe
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
            if cursor.fetchone()[0] > 0:
                return auth_pb2.AuthResponse(success=False, message="Usuário já existe.")

            # Inserir novo usuário
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password_hash))
            conn.commit()

            return auth_pb2.AuthResponse(success=True, message="Usuário registrado com sucesso.")
        
        except Exception as e:
            conn.rollback()
            return auth_pb2.AuthResponse(success=False, message=f"Erro: {str(e)}")
        
        finally:
            cursor.close()
            conn.close()

    def Login(self, request, context):
        email = request.email
        password_hash = hashlib.sha256(request.password.encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Verificar se o usuário existe e se a senha está correta
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s AND password = %s", (email, password_hash))
            if cursor.fetchone()[0] == 0:
                return auth_pb2.AuthResponse(success=False, message="Usuário ou senha incorretos.", token = None)

            return auth_pb2.AuthResponse(success=True, message="Login bem-sucedido.", token = generate_token(email))
        
        except Exception as e:
            return auth_pb2.AuthResponse(success=False, message=f"Erro: {str(e)}", token = None)
        
        finally:
            cursor.close()
            conn.close()

    def ListUsers(self, request, context):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            resposta , motivo = verify_token(request.token)

            if resposta :
                cursor.execute("SELECT email FROM users")
                users = cursor.fetchall()
                for user in users:
                    yield auth_pb2.User(email=user[0])
            else:
                yield auth_pb2.User(email=f"Erro: {motivo}")
            
        
        except Exception as e:
            yield auth_pb2.User(email=f"Erro: {str(e)}")
        
        finally:
            cursor.close()
            conn.close()



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC escutando na porta 50051...")
    server.wait_for_termination()
    
def verificar_email(email: str) -> dict:
    # Sua chave da API do Hunter.io
    api_key = "111a8bf107ec70cf1e95fdfb2d3a797da86bf03f"
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    
    # Faz a requisição GET para a API do Hunter.io
    response = requests.get(url, verify=False)
    
    # Verifica o status da resposta
    if response.status_code == 200:
        data = response.json()
        # Retorna o resultado da verificação
        return data['data']
    else:
        # Retorna um erro se a requisição falhar
        return {"error": "Não foi possível verificar o e-mail"}

if __name__ == '__main__':
    serve()

