# Generated by Django 3.2.7 on 2023-01-13 17:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('karseva', '0018_auto_20230113_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='lastModifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestCreatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestTimeInBound',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requestTimeOutBound',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesubcategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 13, 17, 24, 39, 831477, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='karseva.rating', to_field='ratingName')),
                ('serviceRequest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='karseva.servicerequest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]