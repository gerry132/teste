# Generated by Django 3.2.10 on 2023-11-28 14:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_navigation', '0006_primarynavigation_popular_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarynavigation',
            name='popular_links',
            field=wagtail.fields.StreamField([('popular_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False)), ('url', wagtail.blocks.URLBlock(help_text='An external link.', label='URL', required=False))]))], blank=True, help_text='Popular links for search', use_json_field=True, verbose_name='Popular Links'),
        ),
    ]