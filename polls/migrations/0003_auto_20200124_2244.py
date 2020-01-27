# Generated by Django 3.0.2 on 2020-01-24 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200124_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='questions',
            field=models.ManyToManyField(help_text='Укажите, в какие вопросы хотите добавить участника', to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='final_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 25, 19, 44, 36, 905105, tzinfo=utc), verbose_name='Дата окончания'),
        ),
    ]