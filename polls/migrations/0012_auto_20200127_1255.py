# Generated by Django 3.0.2 on 2020-01-27 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200126_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='photo_person',
            field=models.ImageField(blank=True, height_field=100, upload_to='person/photos', width_field=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='final_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 28, 9, 55, 52, 346498, tzinfo=utc), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 27, 9, 55, 52, 346498, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]