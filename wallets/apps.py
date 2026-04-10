from django.apps import AppConfig


class walletsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wallets'

    def ready(self):
        import wallets.signals # Import the signals to ensure they are registered when the app is ready




# Create your models here.
