from cost_accounting_manager.celery import app

from .services import send_email


@app.task
def send_statistics_email():
    send_email()
