# Generated by Django 3.2.10 on 2024-01-10 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0013_footernavigation_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footernavigation',
            name='lang',
        ),
    ]
