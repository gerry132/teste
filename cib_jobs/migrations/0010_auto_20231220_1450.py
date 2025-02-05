# Generated by Django 3.2.10 on 2023-12-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_jobsvacanciesandlatestnewssnippet'),
        ('cib_jobs', '0009_auto_20231220_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobvacanciestag',
            options={'verbose_name': 'job company tag', 'verbose_name_plural': 'job company tags'},
        ),
        migrations.AddField(
            model_name='jobvacanciespage',
            name='jobvacancy_latestnews_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.jobsvacanciesandlatestnewssnippet'),
        ),
        migrations.AddField(
            model_name='jobvacanciespage',
            name='news_letter_signup_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.newslettersignupctasnippet'),
        ),
    ]
