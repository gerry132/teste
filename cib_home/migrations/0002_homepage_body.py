# Generated by Django 3.2.10 on 2023-11-23 14:28

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('CalloutCards', wagtail.blocks.StructBlock([('calloutcards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
