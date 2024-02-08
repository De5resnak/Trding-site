from django.apps import AppConfig


class TradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trade'

    def ready(self):
        from django.contrib.auth.models import User
        from .models import MemberUser
        import trade.signals
