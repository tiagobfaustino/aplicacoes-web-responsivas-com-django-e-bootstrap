# Generated by Django 4.2.2 on 2023-06-09 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_subtitle_post_subtitulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 18, 34, 51, 768202, tzinfo=datetime.timezone.utc)),
        ),
    ]
