from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals


red = redis.Redis(
    host='redis-14707.c124.us-central1-1.gce.redns.redis-cloud.com',
    port=14707,
    password='8Xjw6MrT6ZKicvF3vdawCa7PcPv0vM3f'
)