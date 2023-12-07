# Generated by Django 3.2.10 on 2023-12-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cib_documents', '0002_customdocument_uploaded_by_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTypeTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('description', models.CharField(default='', max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Publication Type Tag',
                'verbose_name_plural': 'Publication Type Tags',
            },
        ),
        migrations.CreateModel(
            name='YearTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
                ('description', models.CharField(default='', max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Year Tag',
                'verbose_name_plural': 'Year Tags',
            },
        ),
    ]