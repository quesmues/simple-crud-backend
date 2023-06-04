# Simple CRUD Backend

Porjeto criado com o intuito de implementar uma API de CRUD para a criação de Usuário, e realizar geração de token JWT para login.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### Pré-requisitos

Instale o Python 3.10.

Consulte **Variáveis de ambiente** para configurar as váriaveis de ambiente.

### Instalação

Para rodar o projeto em seu computador, primeiro instale os depências com:

```
pip install -r api/requirements.txt
```

Iniciar o FastAPI em modo de desenvolvimento:

```
uvicorn api.main:app --reload
```

Para verificar se o projeto está rodando abra no seu navegador e insira o endereço abaixo.

```
http://127.0.0.1:8000/docs
```

Caso retorne o swagger com a documentação do projeto, o projeto está funcionado!

## Endpoints

E os endpoints implementados são:

```
GET http://127.0.0.1:8000/api/v1/usuario
POST http://127.0.0.1:8000/api/v1/usuario
GET http://127.0.0.1:8000/api/v1/usuario/<id>/

POST http://127.0.0.1:8000/api/v1/login
```

## Variáveis de Ambiente

Antes de rodar ou implementar o ambiente, copiar o arquivo "api/.env.example" para "api/.env".

E realizar a configuração conforme abaixo.

```
DEBUG //Modo de debug

DATABASE_URL //URL do banco de dados

CORS_ALLOW_ORGINS //Domínio permitido para chamadas Cross-Origin das API's 

# JWT Configs

JWT_SECRET_KEY // Chave secreta para geração do token de acesso
JWT_REFRESH_SECRET_KEY // Chave secreta para geração do token de refresh

```

## Implantação

E para implementar o servidor produtivo, instalar o docker e executar o comando abaixo:

Nota: Lembre-se de passar o valor dos argumentos no build pois é necessário para instalar o AWS Cli

```
docker-compose up --build
```

A imagem será construida e o projeto estará rodando em um container.

Ou se prefir utilizar um servidor produtivo que tenha suporte para uso da app do FastAPI.

Exemplo com o Uvicorn:

```
uvicorn api.main:app
```

## Tests

Os tests foram feitos utilizando o pytest, para executar apenas rodar o comando abaixo.

```
pytest
```

## Construído com

FastAPI, SQLAlchemy.

## Autor

* **Eduardo Czamanski Rota** - *Trabalho Inicial* - [Eduardo C. Rota](https://github.com/quesmues)
