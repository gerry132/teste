import csv
import hashlib
import os
import random

from django.conf import settings
from django.core.validators import URLValidator
from django.db import models
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class Address(models.Model, index.Indexed):
    unique_id = models.CharField(max_length=20, editable=False, unique=True)
    title = models.CharField(max_length=150)
    orgname = models.CharField(max_length=150, verbose_name="Organisation name")
    dept = models.CharField(max_length=150, blank=True,
                            null=True, verbose_name="Department")
    address = models.TextField(max_length=300, blank=True, null=True)
    opening = models.CharField(blank=True, null=True,
                               max_length=200, verbose_name="Opening hours")
    phone = models.CharField(max_length=100, blank=True, null=True)
    locall = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    homepage = models.CharField(max_length=250, blank=True, null=True, validators=[URLValidator()])
    homepage2 = models.CharField(max_length=250, blank=True, null=True, validators=[URLValidator()])
    email = models.EmailField(blank=True, null=True)
    contact_form = models.CharField(max_length=150, blank=True, null=True, verbose_name="Contact Form")
    longitude = models.CharField(max_length=20, blank=True, null=True, editable=False)
    latitude = models.CharField(max_length=20, blank=True, null=True, editable=False)
    # Irish data
    orgname_ga = models.CharField(max_length=150, blank=True,
                                  null=True, verbose_name="Organisation name (Gaeilge)")
    dept_ga = models.CharField(max_length=150, blank=True,
                               null=True, verbose_name="Department (Gaeilge)")
    address_ga = models.TextField(max_length=300, blank=True,
                                  null=True, verbose_name="Address (Gaeilge)")
    opening_ga = models.CharField(blank=True, null=True,
                                  max_length=200, verbose_name="Opening hours (Gaeilge)")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "addresses"
        ordering = ["title"]

    def save(self, *args: list, **kwargs: dict) -> None:
        # setting a random hash as the unique_id
        if not self.unique_id:
            m = hashlib.md5(usedforsecurity=False)  # nosec
            seed = str(random.randint(1, 10000000)).encode()
            m.update(seed)
            self.unique_id = "a" + m.hexdigest()[:10]
        super(Address, self).save(*args, **kwargs)

    @classmethod
    def clear(cls) -> None:
        cls.objects.all().delete()

    @classmethod
    def reset(cls, path: str) -> bool:
        csv_path = "{}/{}".format(settings.BASE_DIR, path)
        if not os.path.exists(csv_path):
            return False
        cls.clear()
        with open(csv_path, newline="") as f:
            reader = csv.reader(f)
            headers = next(reader)
            data = [cls(**dict(zip(headers, row))) for row in reader]
            cls.objects.bulk_create(data)
        return False

    search_fields = [
        index.SearchField('unique_id'),
        index.SearchField('title'),
        index.FilterField('unique_id'),
        index.FilterField('title'),
    ]
