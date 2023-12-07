# Generated by Django 3.2.10 on 2023-12-06 11:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('cib_documents', '0003_documenttypetag_yeartag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('document', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True)), ('language', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))]), label='Languages', required=True)), ('year_tags', wagtail.blocks.ChoiceBlock(choices=[], label='Year Tags', required=False)), ('document_type_tags', wagtail.blocks.ChoiceBlock(choices=[], label='Document Type Tags', required=False))]))], blank=True, use_json_field=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
