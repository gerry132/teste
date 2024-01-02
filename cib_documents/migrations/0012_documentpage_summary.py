# Generated by Django 3.2.10 on 2024-01-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cib_documents', '0011_documenttypetag_locale'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpage',
            name='summary',
            field=models.TextField(blank=True, help_text='Summary text to appear under search results', null=True),
        ),
    ]
