# Generated by Django 4.2.2 on 2023-06-09 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 22, 58, 50, 657233, tzinfo=datetime.timezone.utc)),
        ),
    ]