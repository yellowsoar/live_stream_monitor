from django.apps import AppConfig


class YoutubeLiveConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "youtube_live"

    def ready(self):
        import youtube_live.signals
