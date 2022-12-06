from time import sleep
from celery import shared_task


@shared_task
def send_name_email(name, email):
    result = send_name_email.delay()
    print(result.backend)
    sleep(10)
    print(name + " " + email)


@shared_task
def add(x, y):
    return x + y