# Generated by Django 3.0.2 on 2020-01-24 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('final_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 25, 13, 42, 4, 496275, tzinfo=utc), verbose_name='Дата окончания')),
                ('win_vote', models.IntegerField(default=-1, verbose_name='Досрочная победа')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0, verbose_name='Количество голосов')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('bio_person', models.TextField(help_text='Кратко об участнике', max_length=500, verbose_name='Краткая биография')),
                ('question', models.ManyToManyField(to='polls.Question', verbose_name='Вопрос')),
            ],
        ),
    ]
