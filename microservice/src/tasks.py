import celery

from src.kernel.actions import test

app = celery.Celery('microservice', broker='redis://0.0.0.0:6379/0')

@app.task(name='microservice.test_task')
def test_task():
    test()
    return 'success'
    