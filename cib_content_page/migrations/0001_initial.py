# Generated by Django 3.2.10 on 2023-12-04 15:58

import cib_content_page.blocks.table
import cib_content_page.blocks.video
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.search.index
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('orgname', models.CharField(max_length=150, verbose_name='Organisation name')),
                ('dept', models.CharField(blank=True, max_length=150, null=True, verbose_name='Department')),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('opening', models.CharField(blank=True, max_length=200, null=True, verbose_name='Opening hours')),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('locall', models.CharField(blank=True, max_length=100, null=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('homepage', models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.URLValidator()])),
                ('homepage2', models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.URLValidator()])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_form', models.CharField(blank=True, max_length=150, null=True, verbose_name='Contact Form')),
                ('longitude', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('latitude', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('orgname_ga', models.CharField(blank=True, max_length=150, null=True, verbose_name='Organisation name (Gaeilge)')),
                ('dept_ga', models.CharField(blank=True, max_length=150, null=True, verbose_name='Department (Gaeilge)')),
                ('address_ga', models.TextField(blank=True, max_length=300, null=True, verbose_name='Address (Gaeilge)')),
                ('opening_ga', models.CharField(blank=True, max_length=200, null=True, verbose_name='Opening hours (Gaeilge)')),
            ],
            options={
                'verbose_name_plural': 'addresses',
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('publication_log', wagtail.fields.RichTextField(blank=True, help_text='Put your comment for current changes', null=True, verbose_name='publication_log')),
                ('body', wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('custom_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='', label='Image')), ('caption', wagtail.blocks.CharBlock(label='Caption', required=False)), ('alt_text', wagtail.blocks.CharBlock(label='Alt', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('200', '200*132'), ('400', '400*267'), ('800', '800*534')], label='Size', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Align', required=False))])), ('video', cib_content_page.blocks.video.VideoBlock()), ('embed_html_widget', wagtail.blocks.TextBlock(required=False)), ('richtext', wagtail.blocks.RichTextBlock(required=False)), ('table', cib_content_page.blocks.table.TinyMCETableBlock()), ('address', wagtail.blocks.StructBlock([('address', wagtail.snippets.blocks.SnippetChooserBlock('cib_core.Address'))])), ('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('anchor_id', wagtail.blocks.CharBlock(help_text='Anchor target must be a compatible slug format without spaces or special characters', label='Anchor ID (Optional)', required=False))]))], blank=True, use_json_field=True, verbose_name='body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('description', models.CharField(default='', max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Page Tag',
                'verbose_name_plural': 'Page Tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='cib_content_page.contentpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_pages', to='cib_content_page.pagetag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contentpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='cib_content_page.TaggedPage', to='cib_content_page.PageTag', verbose_name='Tags'),
        ),
    ]
