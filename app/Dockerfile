# Use uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copia o arquivo de dependências
COPY ./requirements.txt /code/requirements.txt

# Instala as dependências do projeto
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia o restante do código do app
COPY . /code/app

# Expõe a porta do FastAPI
EXPOSE 8000

# Define PYTHONPATH
ENV PYTHONPATH="/app"

# Comando para rodar o aplicativo FastAPI com Uvicorn
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--app-dir", "/app"]
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
