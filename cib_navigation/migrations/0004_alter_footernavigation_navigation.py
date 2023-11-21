# Generated by Django 3.2.10 on 2023-11-17 17:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0003_auto_20231117_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footernavigation',
            name='navigation',
            field=wagtail.fields.StreamField([('two_colum_list', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Leave blank if no header required.', required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))])))])), ('single_colum_list', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='Leave blank if no header required.', required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))])))]))], blank=True, help_text='Multiple columns of footer links with optional header.', use_json_field=None, verbose_name='Columns'),
        ),
    ]
