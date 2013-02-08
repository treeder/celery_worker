from celery import Celery
import iron_celery

celery = Celery('mytasks', broker='ironmq://', backend='ironcache://')

@celery.task
def tadd(x, y):
    return x + y

