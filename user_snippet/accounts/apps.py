from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_snippet.accounts"

    def ready(self):
        """
        Method called when the app is ready.

        This method is executed during Django's startup process when the app is ready to be used.
        It imports the signals module to ensure that the signals are connected and the signal handlers
        are registered when the app is fully loaded and ready to work.
        """
        import user_snippet.accounts.signals
