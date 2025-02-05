# Generated by Django 3.2.10 on 2023-12-14 10:19

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cib_content_page', '0002_alter_contentpage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsContentPage',
            fields=[
                ('contentpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cib_content_page.contentpage')),
                ('banner_image', wagtail.fields.StreamField([('banner_image', wagtail.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(help_text='', label='Image')), ('alt_text', wagtail.blocks.CharBlock(label='Alt', required=False))]))], null=True, use_json_field=True)),
                ('show_on_page', models.BooleanField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cib_content_page.contentpage',),
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'news tag',
                'verbose_name_plural': 'news tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_news_items', to='cib_news_content_page.newscontentpage')),
                ('tag', models.ForeignKey(help_text='news tags', on_delete=django.db.models.deletion.CASCADE, related_name='tagged_news', to='cib_news_content_page.newstag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newscontentpage',
            name='news_tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='cib_news_content_page.NewsTag'),
        ),
    ]
