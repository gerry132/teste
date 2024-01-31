# Generated by Django 3.2.10 on 2024-01-30 10:47

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0016_alter_footernavigation_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarynavigation',
            name='navigation',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))]))], blank=True, help_text='Main site navigation', use_json_field=True, verbose_name='Links'),
        ),
        migrations.AlterField(
            model_name='primarynavigation',
            name='popular_links',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('popular_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))]))], blank=True, help_text='Popular links for search', use_json_field=True, verbose_name='Popular Links'),
        ),
    ]
