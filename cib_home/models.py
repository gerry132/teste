from cib_utils.models import BasePage
from django.db import models

from wagtail.images import get_image_model_string
# Create your models here.

IMAGE_MODEL = get_image_model_string()


class HomePage(BasePage):
    max_count = 1
    template = "patterns/pages/home/home_page.html"
    favicon = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
