from django.db import models


class Category(models.Model):
    ACTION_CHOICE = [
        ('accrue', 'Начислить'),
        ('write_off', 'Списать')
    ]
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=20, choices=ACTION_CHOICE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserTransactions(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sum = models.FloatField()
    time = models.TimeField()
    date = models.DateField()
    category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    organization = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)


class Balance(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
