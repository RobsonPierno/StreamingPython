# Meu Primeiro Projeto Python com FastAPI

Este é meu primeiro projeto em Python, onde exponho APIs utilizando o **FastAPI**. O projeto foi desenvolvido para praticar e aprofundar meus conhecimentos em Python e em desenvolvimento de APIs.

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido (alta performance) para a construção de APIs com Python 3.7+ baseado em tipos e anotações. Ele permite criar APIs RESTful de maneira simples e eficiente.
  
- **Pydantic**: Uma biblioteca que fornece validação de dados e parsing usando anotações de tipo. É utilizado para definir e validar os dados que entram e saem da API.

- **SQLAlchemy**: Um ORM (Object-Relational Mapping) que facilita a interação com bancos de dados, permitindo que você trabalhe com dados como objetos Python, ao invés de SQL puro.

- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional que é utilizado como a base de dados do projeto, onde as informações são armazenadas.

- **httpx**: Uma biblioteca para fazer chamadas HTTP. É utilizada para chamar outros serviços de forma assíncrona, permitindo que o projeto interaja com APIs externas.

- **pydantic-settings**: Uma extensão do Pydantic que facilita a configuração de aplicativos usando variáveis de ambiente e arquivos de configuração.

## Dockerização

O projeto está dockerizado, permitindo que você execute o aplicativo em um ambiente isolado e consistente. Isso facilita a implantação e a execução do projeto em diferentes máquinas.

## Como Iniciar o Projeto

Siga os passos abaixo para configurar e iniciar o projeto localmente:

### 1. Criar um Ambiente Virtual

Primeiro, crie um ambiente virtual para isolar as dependências do seu projeto:

```bash
python -m venv .venv

### 2. Ativar o Ambiente Virtual

Ative o ambiente virtual. O comando varia conforme o sistema operacional:

- **Windows**:
  ```bash
  .venv\Scripts\activate

- **Linux/Mac**:
  ```bash
  source .venv/bin/activate

### 3. Instalar as Dependências

Instale as dependências necessárias para o projeto. Certifique-se de ter um arquivo `requirements.txt` com as bibliotecas necessárias:

```bash
pip install -r requirements.txt

### 4. Iniciar o Projeto

Execute o servidor FastAPI com o seguinte comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
