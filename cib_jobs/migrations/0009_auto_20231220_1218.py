# Generated by Django 3.2.10 on 2023-12-20 12:18

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cib_jobs', '0008_auto_20231220_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobvacanciespage',
            name='company_select_component',
            field=wagtail.fields.StreamField([('publication_select_component', wagtail.blocks.StructBlock([('select_title', wagtail.blocks.CharBlock(max_length=50)), ('select_hint_text', wagtail.blocks.CharBlock(max_length=50, required=False)), ('select_default_option_value', wagtail.blocks.CharBlock(max_length=50))]))], null=True, use_json_field=None),
        ),
        migrations.AddField(
            model_name='jobvacanciespage',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
