from cost_accounting_manager.celery import app
from user_transactions.models import UserTransactions, Category
from user_transactions.services import send_email

from datetime import datetime, timedelta

from django.contrib.auth.models import User


@app.task
def send_statistics_email():
    yesterday_date = datetime.now().date() - timedelta(days=1)
    users = User.objects.filter(is_staff=False).values_list('id', 'username')
    for user in users:
        user_id = user[0]
        user_name = user[1]
        statistic = UserTransactions.objects.filter(owner=user_id, date=yesterday_date).count()
        cat_id = UserTransactions.objects.filter(owner=user, date=yesterday_date).values_list('category', flat=True)
        sum_day = 0
        for cat in cat_id:
            cat_name = Category.objects.filter(id=cat).values_list('action', flat=True).get()
            if cat_name == 'write_off':
                sum = UserTransactions.objects.filter(owner=user,
                                                      date=yesterday_date,
                                                      category=cat).values_list('sum', flat=True).get()
                sum_day += sum
        owner_email = User.objects.filter(id=user_id).values_list('email').get()
        send_email(statistic, sum_day, owner_email, yesterday_date, user_name)
