# Generated by Django 3.2.10 on 2023-12-08 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersignupctasnippet',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
        ),
        migrations.AddField(
            model_name='newslettersignupctasnippet',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='newslettersignupctasnippet',
            name='button_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newslettersignupctasnippet',
            name='snippet_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newslettersignupctasnippet',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='newslettersignupctasnippet',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='newslettersignupctasnippet',
            unique_together={('translation_key', 'locale')},
        ),
    ]
