# Generated by Django 3.1.7 on 2021-04-04 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20210328_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
