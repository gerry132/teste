from django.apps import AppConfig


class CibNewsContentPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cib_news_content_page'

    def ready(self):
        import cib_news_content_page.signals  # noqa