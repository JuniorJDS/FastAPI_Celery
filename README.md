# FastAPI_Celery

### Criando um ambiente Virtual e Instalando os requirements

```
$ python3 -m venv venv

$ source venv/bin/activate

$ pip3 install --upgrade pip

$ pip3 install -r requirements.txt

```

## Como rodar?

### 1- FastAPI - http://localhost:8000/docs
```
$ uvicorn main:app --reload

```

### 2- Celery
```
$ celery -A celery_worker.celery worker --loglevel=info

```

### 3- Flower - http://localhost:5555/ 
```
$ celery flower -A celery_worker.celery --broker:amqp://localhost//

```