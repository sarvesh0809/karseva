# Generated by Django 3.2.7 on 2023-01-30 11:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('karseva', '0039_auto_20230129_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='lastModifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestCreatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='volunteerPoint',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='taskactivity',
            name='time_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 30, 11, 28, 24, 447829, tzinfo=utc)),
        ),
    ]
