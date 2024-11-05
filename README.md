# Projeto de Autenticação gRPC com JWT

Este projeto implementa um sistema de autenticação distribuído usando **gRPC** e **JWT** para segurança e autenticação de usuários. O servidor é responsável por gerenciar registros, logins e listagem de usuários, com suporte para verificação de e-mails usando a API do **Hunter.io**.

## Descrição dos Arquivos

- `auth.proto`: Define os serviços e mensagens gRPC para registro, login e listagem de usuários.
- `server.py`: Implementa o servidor gRPC com funcionalidades de registro, login, geração de tokens JWT e listagem de usuários.
- `client.py`: Cliente gRPC com um menu interativo para registro, login e listagem de usuários autenticados.
- `README.md`: Documentação do projeto, com instruções de instalação e uso.

## Requisitos

Este projeto requer Python 3.10.5 e as seguintes bibliotecas:

- grpcio e grpcio-tools
- PyJWT (para manipulação de tokens JWT)
- psycopg2 (para conexão com o banco de dados PostgreSQL)
- requests (para fazer requisições à API do Hunter.io)

## Instalação

1. Clone o repositório:
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>

2. Instale as dependências:
   pip install grpcio grpcio-tools PyJWT psycopg2 requests

3. Compile o arquivo `.proto`:
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. auth.proto

4. Configure a variável de ambiente para a chave de API do **Hunter.io**: (opcional)
   - Crie uma conta no Hunter.io e obtenha uma chave de API.
   - Configure a chave de API como uma variável de ambiente:
     export HUNTER_API_KEY='sua_chave_da_api'

## Configuração do Banco de Dados

O servidor usa um banco de dados PostgreSQL hospedado para armazenar e gerenciar informações de usuários.

Se você tiver seu próprio banco de dados PostgreSQL, atualize as configurações em `server.py`:

db_config = {
    'dbname': 'nome_do_banco',
    'user': 'usuario',
    'password': 'senha',
    'host': 'host_do_banco',
    'port': '5432',
}

## Como Executar

### Servidor

1. Em um terminal, execute o servidor:
   python server.py
   O servidor estará escutando na porta `50051`.

### Cliente

1. Em outro terminal, execute o cliente:
   python client.py
   O cliente apresenta um menu com as seguintes opções:
   - Registrar novo usuário
   - Fazer login
   - Listar usuários cadastrados (necessário estar autenticado com JWT)
   - Sair

## Como Usar

1. **Registrar Usuário**:
   - Escolha a opção `1` no menu para registrar um novo usuário com e-mail e senha.
   - O servidor validará o e-mail com a API do Hunter.io.

2. **Login**:
   - Escolha a opção `2` para fazer login. Um token JWT é gerado e armazenado no cliente após login bem-sucedido.

3. **Listar Usuários**:
   - Escolha a opção `3` para listar todos os usuários. O servidor verificará o token JWT antes de retornar a lista.

4. **Sair**:
   - Escolha a opção `4` para sair do cliente.

## Estrutura do Projeto


- auth_pb2_grpc.py             
- auth_pb2.py             
- auth.proto             # Definição do serviço gRPC
- server.py              # Implementação do servidor gRPC
- client.py              # Implementação do cliente gRPC com menu interativo
- README.md              # Documentação do projeto

## Considerações

Este projeto demonstra o uso de gRPC com autenticação JWT em um sistema distribuído. É uma base sólida para aplicações que requerem autenticação segura e comunicação eficiente entre cliente e servidor.
