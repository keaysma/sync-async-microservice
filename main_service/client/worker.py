import celery
from requests import get
from .constants import TEST_TASK

celery_app = celery.Celery('microservice', broker='redis://0.0.0.0:6379/0')

class TestTask():
    @staticmethod
    def run_sync():
        return get('http://0.0.0.0:5000/test')

    @staticmethod
    def run_async():
        return celery_app.signature(TEST_TASK).delay()