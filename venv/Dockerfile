FROM sanicframework/sanic:3.9-latest

WORKDIR /sanic

COPY src/ .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PG_HOSTNAME="pg-container"

EXPOSE 8000

CMD ["python", "server.py"]