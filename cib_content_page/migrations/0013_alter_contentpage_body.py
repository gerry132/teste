# Generated by Django 3.2.10 on 2024-04-08 11:50

import cib_content_page.blocks.table
import cib_content_page.blocks.video
import cib_documents.models
from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cib_content_page', '0012_alter_contentpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('custom_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='', label='Image')), ('caption', wagtail.blocks.CharBlock(label='Caption', required=False)), ('caption_align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Caption Align', required=False)), ('alt_text', wagtail.blocks.CharBlock(label='Alt', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('200', '200*132'), ('400', '400*267'), ('800', '800*534'), ('FullWidth', 'Full Width')], label='Size', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Align', required=False))])), ('video', cib_content_page.blocks.video.VideoBlock()), ('embed_html_widget', wagtail.blocks.TextBlock(required=False)), ('richtext', wagtail.blocks.RichTextBlock(required=False)), ('table', cib_content_page.blocks.table.TinyMCETableBlock()), ('address', wagtail.blocks.StructBlock([('address', wagtail.snippets.blocks.SnippetChooserBlock('cib_content_page.Address'))])), ('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('anchor_id', wagtail.blocks.CharBlock(help_text='Anchor target must be a compatible slug format without spaces or special characters', label='Anchor ID (Optional)', required=False))])), ('document', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(help_text='A short one-sentence literal description\n                    of the image is\n                    required to make the page accessible to the\n                    visually impaired. Details: https://axesslab.com/alt-texts/', required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=True)), ('language', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Language Title', required=True)), ('languages', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.ChoiceBlock(choices=[('English', 'English'), ('Gaeilge', 'Gaeilge')], label='Heading')), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))]), label='Languages', required=True))], label='Languages', required=True)), ('year_tags', wagtail.blocks.ChoiceBlock(choices=cib_documents.models.get_year_tag_choices, label='Year Tags', required=False)), ('publication_type_tags', wagtail.blocks.ChoiceBlock(choices=cib_documents.models.get_document_type_tag_choices, label='Publication Type Tags', required=False))]))], blank=True, use_json_field=True, verbose_name='body'),
        ),
    ]
