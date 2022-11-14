from django.core.mail import send_mail

from .models import Balance, UserTransactions, Category
from django.db import transaction

from django.conf import settings


def make_transaction(owner, sum, time, date, category, organization, description):
    balance = Balance.objects.values_list('balance', flat=True).get(owner=owner)
    cat_action = Category.objects.values_list('action', flat=True).get(id=category)
    cat = Category.objects.only('id').get(id=category)

    if cat_action == 'write_off' and balance < sum:
        return False
    else:
        with transaction.atomic():
            if cat_action == 'accrue':
                balance += sum
                Balance.objects.filter(owner=owner).update(balance=balance)
            else:
                balance -= sum
                Balance.objects.filter(owner=owner).update(balance=balance)

        UserTransactions.objects.create(
            sum=sum,
            time=time,
            date=date,
            organization=organization,
            description=description,
            owner=owner,
            category=cat
        )
    return True


def send_email(statistic, sum, owner_email, yesterday_date, user_name):
    send_mail(
        subject='Hi',
        message=f'Добрый день, {user_name}! '
                f'Вы {yesterday_date} добивили {statistic} записи на сумму {sum}.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=owner_email,
        fail_silently=False,
    )
