# Generated by Django 3.2.7 on 2023-01-11 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('karseva', '0009_auto_20230111_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 12, 58, 35, 566484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 12, 58, 35, 566484, tzinfo=utc)),
        ),
    ]