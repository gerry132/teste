# Generated by Django 3.2.10 on 2024-01-03 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0008_auto_20240103_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='site_logo_alt',
            new_name='site_english_logo_alt',
        ),
    ]
