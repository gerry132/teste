# Generated by Django 3.2.10 on 2024-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0015_footernavigation_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footernavigation',
            name='lang',
            field=models.CharField(help_text="Internal name for this navigation, it's not displayed to a site user.", max_length=255, unique=True, verbose_name='Language'),
        ),
    ]