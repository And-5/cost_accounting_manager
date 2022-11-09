from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category, Balance


@receiver(post_save, sender=User)
def post_sss(created, **kwargs):
    instance = kwargs['instance']

    if created:
        Category.objects.bulk_create([
            Category(name='Забота о себе', action='write_off', owner=instance),
            Category(name='Зарплата', action='accrue', owner=instance),
            Category(name='Здоровье и фитнес', action='write_off', owner=instance),
            Category(name='Кафе и рестораны', action='write_off', owner=instance),
            Category(name='Машина', action='write_off', owner=instance),
            Category(name='Образование', action='write_off', owner=instance),
            Category(name='Отдых и развлечения', action='write_off', owner=instance),
            Category(name='Платежи, комиссии', action='write_off', owner=instance),
            Category(name='Покупки: одежда, техника', action='write_off', owner=instance),
            Category(name='Продукты', action='write_off', owner=instance),
            Category(name='Проезд', action='write_off', owner=instance),
        ]),

        Balance.objects.create(owner=instance)
