# Generated by Django 3.2.10 on 2024-01-31 10:51

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0017_auto_20240130_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarynavigation',
            name='navigation',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))]))], blank=True, help_text='Main site navigation', use_json_field=True, verbose_name='Links'),
        ),
    ]
