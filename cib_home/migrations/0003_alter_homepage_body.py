# Generated by Django 3.2.10 on 2023-11-23 14:31

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cib_home', '0002_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('CalloutCards', wagtail.blocks.StructBlock([('calloutcards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
