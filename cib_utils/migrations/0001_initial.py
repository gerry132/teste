# Generated by Django 3.2.10 on 2023-12-04 11:45

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.models
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cib_images', '0002_initial'),
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSignUpCTASnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes')),
                ('first_published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at')),
                ('last_published_at', models.DateTimeField(editable=False, null=True, verbose_name='last published at')),
                ('go_live_at', models.DateTimeField(blank=True, null=True, verbose_name='go live date/time')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time')),
                ('expired', models.BooleanField(default=False, editable=False, verbose_name='expired')),
                ('snippet_title', models.CharField(max_length=255)),
                ('icon_alt', models.CharField(blank=True, help_text='The alt text shown for accessibility: https://axesslab.com/alt-texts/', max_length=255, verbose_name='Icon Alt text')),
                ('title', models.CharField(max_length=255)),
                ('body', wagtail.fields.RichTextField(blank=True, null=True)),
                ('button_text', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cib_images.customimage')),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
                ('live_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.models.PreviewableMixin, wagtail.search.index.Indexed, models.Model),
        ),
    ]
