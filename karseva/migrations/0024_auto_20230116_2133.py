# Generated by Django 3.2.7 on 2023-01-16 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('karseva', '0023_auto_20230115_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requeststatus',
            name='statusName',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='lastModifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestCreatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestTimeInBound',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestTimeOutBound',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 16, 16, 3, 36, 530506, tzinfo=utc)),
        ),
    ]
