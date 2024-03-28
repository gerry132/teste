# Generated by Django 3.2.10 on 2024-03-28 12:57

import cib_content_page.blocks.table
import cib_content_page.blocks.video
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.forms.models
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cib_content_page', '0012_alter_contentpage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('contentpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cib_content_page.contentpage')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, validators=[wagtail.contrib.forms.models.validate_to_address], verbose_name='to address')),
                ('from_address', models.EmailField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('bottom_page_body', wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('custom_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='', label='Image')), ('caption', wagtail.blocks.CharBlock(label='Caption', required=False)), ('caption_align', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Caption Align', required=False)), ('alt_text', wagtail.blocks.CharBlock(label='Alt', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('200', '200*132'), ('400', '400*267'), ('800', '800*534'), ('FullWidth', 'Full Width')], label='Size', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Centre'), ('right', 'Right')], label='Align', required=False))])), ('video', cib_content_page.blocks.video.VideoBlock()), ('embed_html_widget', wagtail.blocks.TextBlock(required=False)), ('richtext', wagtail.blocks.RichTextBlock(required=False)), ('table', cib_content_page.blocks.table.TinyMCETableBlock()), ('address', wagtail.blocks.StructBlock([('address', wagtail.snippets.blocks.SnippetChooserBlock('cib_content_page.Address'))])), ('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('anchor_id', wagtail.blocks.CharBlock(help_text='Anchor target must be a compatible slug format without spaces or special characters', label='Anchor ID (Optional)', required=False))]))], blank=True, use_json_field=True)),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.forms.models.FormMixin, 'cib_content_page.contentpage', models.Model),
        ),
        migrations.CreateModel(
            name='RichTextFieldLabelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('richtext_label', wagtail.fields.RichTextField(blank=True, help_text='This will show only in the Checkbox fields, this has higher priority than the label field', verbose_name='Rich Text Label')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='cib_form.formpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
