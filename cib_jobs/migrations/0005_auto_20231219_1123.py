# Generated by Django 3.2.10 on 2023-12-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cib_jobs', '0004_auto_20231219_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobvacanciestag',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='jobvacanciestag',
            name='locale',
            field=models.CharField(blank=True, default='en', max_length=10, null=True),
        ),
    ]
