# Generated by Django 3.2.7 on 2023-01-19 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('karseva', '0031_auto_20230120_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='lastModifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestCreatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 19, 19, 5, 59, 170112, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='taskcoordinator_pincode',
        ),
    ]
