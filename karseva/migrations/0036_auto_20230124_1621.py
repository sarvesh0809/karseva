# Generated by Django 3.2.7 on 2023-01-24 10:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('karseva', '0035_auto_20230123_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='lastModifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestCreatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 24, 10, 51, 19, 346332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='taskotp',
            name='service_request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='karseva.servicerequest'),
        ),
    ]
