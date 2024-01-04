# Generated by Django 3.2.10 on 2023-12-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cib_content_page', '0003_contentpage_last_published_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetag',
            name='locale',
            field=models.CharField(default='en', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pagetag',
            name='description',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='description'),
        ),
    ]