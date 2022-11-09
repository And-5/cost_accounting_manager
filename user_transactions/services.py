from .models import Balance, UserTransactions, Category
from django.db import transaction


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
