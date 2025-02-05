# Generated by Django 3.2.10 on 2023-12-07 16:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('publication_log', wagtail.fields.RichTextField(blank=True, help_text='Put your comment for current changes', null=True, verbose_name='publication_log')),
            ],
            options={
                'verbose_name': 'news page',
                'verbose_name_plural': 'news pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
