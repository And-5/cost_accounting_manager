from django.apps import AppConfig


class UserTransactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_transactions'

    def ready(self):
        import user_transactions.signals
