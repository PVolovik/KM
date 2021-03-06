# Generated by Django 3.0.2 on 2020-01-26 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200126_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='person_choice',
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(blank=True, help_text='Укажите, в каком опросе нужно участвовать', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='final_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 27, 19, 12, 46, 345381, tzinfo=utc), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 26, 19, 12, 46, 345381, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
