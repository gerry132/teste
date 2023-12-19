# Generated by Django 3.2.10 on 2023-12-19 11:52

import cib_home.blocks
from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.models
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('utils', '0004_auto_20231208_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsVacanciesAndLatestNewsSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes')),
                ('first_published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at')),
                ('last_published_at', models.DateTimeField(editable=False, null=True, verbose_name='last published at')),
                ('go_live_at', models.DateTimeField(blank=True, null=True, verbose_name='go live date/time')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time')),
                ('expired', models.BooleanField(default=False, editable=False, verbose_name='expired')),
                ('snippet_title', models.CharField(blank=True, max_length=255)),
                ('body', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('job_vacancies', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 60x60 pixels', required=False)), ('icon_alt', wagtail.blocks.CharBlock(help_text='The alt text shown for accessibility: https://axesslab.com/alt-texts/', required=True)), ('vacancy_title', wagtail.blocks.CharBlock(required=True)), ('vacancy_text', wagtail.blocks.RichTextBlock(required=True)), ('vacancy_button_page', wagtail.blocks.PageChooserBlock(help_text='This button has higher priority than button_url', required=False)), ('vacancy_button_url', wagtail.blocks.URLBlock(required=False)), ('vacancies_button_text', wagtail.blocks.CharBlock(help_text='Job vacancies button text', required=True)), ('vacancies_background_color', cib_home.blocks.ColorChooserBlock(help_text='Set the Job vacancies background color', required=True))])), ('news_card', wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='The Icon size should be 60x60 pixels', required=False)), ('icon_alt', wagtail.blocks.CharBlock(help_text='The alt text shown for accessibility: https://axesslab.com/alt-texts/', required=True)), ('block_title', wagtail.blocks.CharBlock(required=True)), ('news_button_text', wagtail.blocks.CharBlock(help_text='News card button text', required=True)), ('news_Background_color', cib_home.blocks.ColorChooserBlock(help_text='Set the News background color', required=True))]))]))], blank=True, use_json_field=None)),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
                ('live_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision')),
                ('locale', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale')),
            ],
            options={
                'unique_together': {('translation_key', 'locale')},
            },
            bases=(wagtail.models.PreviewableMixin, wagtail.search.index.Indexed, models.Model),
        ),
    ]
