FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# CMD ["python", "embeddings_generator.py", "&&", "python", "app.py"]