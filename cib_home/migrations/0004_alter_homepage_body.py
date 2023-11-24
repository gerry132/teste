# Generated by Django 3.2.10 on 2023-11-24 11:53

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_home', '0003_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('CalloutCards', wagtail.blocks.StructBlock([('calloutcards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 55x55 pixels', required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(required=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
