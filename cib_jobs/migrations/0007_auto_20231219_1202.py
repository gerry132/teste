# Generated by Django 3.2.10 on 2023-12-19 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_jobsvacanciesandlatestnewssnippet'),
        ('cib_jobs', '0006_jobvacancycontentpage_jobvacancy_latestnews_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobvacancycontentpage',
            name='jobvacancy_latestnews_snippet',
        ),
        migrations.AddField(
            model_name='jobvacancycontentpage',
            name='jobvacancy_latestnews_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.jobsvacanciesandlatestnewssnippet'),
        ),
    ]