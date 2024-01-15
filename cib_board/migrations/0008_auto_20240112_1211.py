# Generated by Django 3.2.10 on 2024-01-12 12:11

import cib_content_page.blocks.table
import cib_content_page.blocks.video
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_jobsvacanciesandlatestnewssnippet'),
        ('cib_board', '0007_alter_boardpage_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardpage',
            name='jobvacancy_latestnews_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.jobsvacanciesandlatestnewssnippet'),
        ),
        migrations.AddField(
            model_name='boardpage',
            name='news_letter_signup_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.newslettersignupctasnippet'),
        ),
        migrations.AlterField(
            model_name='boardpage',
            name='body',
            field=wagtail.fields.StreamField([('BoardMembersCards', wagtail.blocks.StructBlock([('boardmemberscards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(help_text='A short one-sentence literal description\n                    of the image is\n                    required to make the page accessible to the\n                    visually impaired. Details: https://axesslab.com/alt-texts/', required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.RichTextBlock(required=False))])))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('custom_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='', label='Image')), ('caption', wagtail.blocks.CharBlock(label='Caption', required=False)), ('alt_text', wagtail.blocks.CharBlock(label='Alt', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('200', '200*132'), ('400', '400*267'), ('800', '800*534')], label='Size', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Align', required=False))])), ('video', cib_content_page.blocks.video.VideoBlock()), ('embed_html_widget', wagtail.blocks.TextBlock(required=False)), ('richtext', wagtail.blocks.RichTextBlock(required=False)), ('table', cib_content_page.blocks.table.TinyMCETableBlock()), ('address', wagtail.blocks.StructBlock([('address', wagtail.snippets.blocks.SnippetChooserBlock('cib_content_page.Address'))])), ('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('anchor_id', wagtail.blocks.CharBlock(help_text='Anchor target must be a compatible slug format without spaces or special characters', label='Anchor ID (Optional)', required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
