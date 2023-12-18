from .models import NewsContentPage
from django.utils import timezone

from wagtail.core.signals import page_published


def update_last_published_custom(sender, instance, **kwargs):
    # Update last_published_custom with the current date and time
    if instance.last_published_custom is None:
        instance.last_published_custom = timezone.now().date()
        instance.save()


page_published.connect(
    update_last_published_custom,
    sender=NewsContentPage)
