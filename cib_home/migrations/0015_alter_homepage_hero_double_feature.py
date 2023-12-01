# Generated by Django 3.2.10 on 2023-11-30 15:04

import cib_utils.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_home', '0014_auto_20231130_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_double_feature',
            field=wagtail.fields.StreamField([('feature_block', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading', wagtail.blocks.CharBlock(help_text='Text to display as feature heading', max_length=250, required=False)), ('main_feature', wagtail.blocks.StreamBlock([('rich_text', cib_utils.blocks.RichTextBlock()), ('links_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))], max=5)))])), ('button', wagtail.blocks.StreamBlock([('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(max_length=50)), ('page', wagtail.blocks.PageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False)), ('link_button_alt', wagtail.blocks.CharBlock(help_text='A short one-sentence literal description\n                    of the button is\n                    required to make the page accessible to the\n                    visually impaired. Details: https://axesslab.com/alt-texts/', required=False))], max=1))], max_num=1, required=False)), ('colour_palette', wagtail.blocks.ChoiceBlock(choices=[('base-feature--green', 'Green and Black'), ('base-feature--blue', 'Blue & White')]))]))], blank=True, use_json_field=None),
        ),
    ]
