# Generated by Django 3.2.10 on 2023-11-30 12:08

import cib_home.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_home', '0013_homepage_callout_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('CalloutCards', wagtail.blocks.StructBlock([('calloutcards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 55x55 pixels', required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(required=True)), ('left_border_color', cib_home.blocks.ColorChooserBlock(required=True))]), max_num=3))])), ('InfoPanelCards', wagtail.blocks.StructBlock([('infocards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 60x60 pixels', required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(required=True))])))])), ('JobVacanciesAndNewsCard', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 60x60 pixels', required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(required=True)), ('Job_vacancies_Background_color', cib_home.blocks.ColorChooserBlock(help_text='Set the Job vacancies background color', required=True)), ('news_button_text', wagtail.blocks.CharBlock(help_text='News card button text', required=True)), ('news_Background_color', cib_home.blocks.ColorChooserBlock(help_text='Set the News background color', required=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='callout_feature',
            field=wagtail.fields.StreamField([('callout_cards', wagtail.blocks.StructBlock([('calloutcards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 55x55 pixels', required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(required=True)), ('left_border_color', cib_home.blocks.ColorChooserBlock(required=True))]), max_num=3))]))], blank=True, use_json_field=None),
        ),
    ]