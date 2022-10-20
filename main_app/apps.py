from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

    # overrid the Ready() method 
    def ready(self):
        import main_app.signals


