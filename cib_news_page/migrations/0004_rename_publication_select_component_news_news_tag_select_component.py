# Generated by Django 3.2.10 on 2023-12-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cib_news_page', '0003_auto_20231221_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='publication_select_component',
            new_name='news_tag_select_component',
        ),
    ]
