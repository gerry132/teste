# Generated by Django 3.2.10 on 2023-12-04 15:23

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_pages', '0004_alter_freeformpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeformpage',
            name='publication_log',
            field=wagtail.fields.RichTextField(blank=True, help_text='Put your comment for current changes', null=True, verbose_name='publication_log'),
        ),
    ]