# sync-async-microservice
A little demo on a microservice that relies on sync behavior through flask, and async behavior through celery

## Prep
Setup envs for all three parts
Some time soon include requirement.txt files but there are so few dependencies for me do that right this second

1. main_service
This emulates a monolithic service that's being split into parts, and is now calling a new microservice
```bash
python -m venv .
source bin/activate
pip install flask celery
pip install -U "celery[redis]"
```

2. microservice
This is our microservice, it has a flask endpoint in webserver.py, and a celery task in tasks.py,
these listeners both expose tasks in the kernel directory, as of now there's just a 'test' task
```bash
python -m venv .
source bin/activate
pip install flask celery
pip install -U "celery[redis]"
```

3. reciever
This emulates some other endpoint that our microservice may hit, it's just a dummy to measure work output
```bash
python -m venv .
source bin/activate
pip install flask
```

## Run me
1. Start redis
```bash
redis-server
```

2. Start `receiver`
```bash
cd reciever
python main.py
```
2. Start `microservice`, requires two windows
```bash
cd microservice
python src/webserver.py
```
```bash
cd microservice
python -m celery src.tasks worker -l INFO
```
2. Start `main_service`
```bash
cd main_service
python main.py
```