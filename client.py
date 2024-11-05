import grpc
import auth_pb2
import auth_pb2_grpc
import threading


token_global = None


def register_user(stub, email, password):
    response = stub.Register(auth_pb2.RegisterRequest(email=email, password=password))
    print(f"Registro: {response.message}")

def login_user(stub, email, password):
    global token_global
    response = stub.Login(auth_pb2.LoginRequest(email=email, password=password))
    token_global =  response.token
    print(f"Login: {response.message}")
    #print(token_global)
    

def list_users(stub, token_atual):
    print("Usuários cadastrados:")
    try:
        for user in stub.ListUsers(auth_pb2.ListUsersRequest(token = token_atual)):
            print(" -", user.email)
    except grpc.RpcError as e:
        print("Erro ao listar usuários:", e.details())


def menu():
    print("\n=== MENU ===")
    print("1. Registrar novo usuário")
    print("2. Fazer login")
    print("3. Listar usuários")
    print("4. Sair")
    choice = input("Escolha uma opção: ")
    return choice

def wait_for_keypress():
    input("Aperte uma tecla para continuar...")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = auth_pb2_grpc.AuthServiceStub(channel)

        while True:
            choice = menu()
            threads = []

            if choice == '1':
                # Registrar um novo usuário
                email = input("Digite o email para registro: ")
                password = input("Digite a senha para registro: ")
                thread = threading.Thread(target=register_user, args=(stub, email, password))
                threads.append(thread)
            
            elif choice == '2':
                # Fazer login
                email = input("Digite o email para login: ")
                password = input("Digite a senha para login: ")
                thread = threading.Thread(target=login_user, args=(stub, email, password))
                threads.append(thread)
            
            elif choice == '3':
                # Listar todos os usuários
                thread = threading.Thread(target=list_users, args=(stub,token_global))
                threads.append(thread)
            
            elif choice == '4':
                print("Saindo do programa...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                wait_for_keypress()
                continue

            # Iniciar e aguardar finalização das threads
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

            wait_for_keypress()

if __name__ == '__main__':
    run()
