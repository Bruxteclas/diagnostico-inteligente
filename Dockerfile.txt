# Usando a imagem Python 3.10.12
FROM python:3.10.12-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do projeto para o diretório de trabalho
COPY . /app

# Atualizar o pip e instalar as dependências listadas em requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta que o Streamlit usa (opcional)
EXPOSE 8501

# Comando para iniciar o aplicativo Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
