# Generated by Django 3.2.10 on 2023-12-12 12:13

import cib_documents.models
from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_documents', '0005_alter_documentpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='body',
            field=wagtail.fields.StreamField([('document', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(help_text='A short one-sentence literal description\n                    of the image is\n                    required to make the page accessible to the\n                    visually impaired. Details: https://axesslab.com/alt-texts/', required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True)), ('language', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Language Title', required=True)), ('languages', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))]), label='Languages', required=True))], label='Languages', required=True)), ('year_tags', wagtail.blocks.ChoiceBlock(choices=cib_documents.models.get_year_tag_choices, label='Year Tags', required=False)), ('publication_type_tags', wagtail.blocks.ChoiceBlock(choices=cib_documents.models.get_document_type_tag_choices, label='Publication Type Tags', required=False))]))], blank=True, use_json_field=None),
        ),
    ]
