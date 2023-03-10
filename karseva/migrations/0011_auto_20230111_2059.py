# Generated by Django 3.2.7 on 2023-01-11 15:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('karseva', '0010_auto_20230111_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingName', models.CharField(blank=True, choices=[('EXCELLENT', 'EXCELLENT'), ('VERY GOOD', 'VERY GOOD'), ('GOOD', 'GOOD'), ('FAIR', 'FAIR'), ('POOR', 'GOOD'), ('VERY POOR', 'VERY POOR')], max_length=15)),
                ('ratingNumber', models.IntegerField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='usercontactinfo',
            old_name='AlternatePhoneNumber',
            new_name='alternatePhoneNumber',
        ),
        migrations.RenameField(
            model_name='usercontactinfo',
            old_name='EmergencyContactNumber',
            new_name='emergencyContactNumber',
        ),
        migrations.RenameField(
            model_name='usercontactinfo',
            old_name='PrimaryPhoneNumber',
            new_name='primaryPhoneNumber',
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedBy',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_categor_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicecategory',
            name='modifiedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ServiceSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryName', models.CharField(blank=True, max_length=30)),
                ('isActive', models.BooleanField(default=True)),
                ('createdOn', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('modifiedOn', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('createdBy', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('modifiedBy', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_subcategor_modified_by', to=settings.AUTH_USER_MODEL)),
                ('serviceCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karseva.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestTimeInBound', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('requestTimeOutBound', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('actualTimeInBound', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('actualTimeOutBound', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('requestCreatedOn', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('lastModifiedOn', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 11, 15, 29, 35, 860381, tzinfo=utc))),
                ('description', models.CharField(blank=True, max_length=200)),
                ('userFeedback', models.CharField(blank=True, max_length=200)),
                ('volunteerFeedback', models.CharField(blank=True, max_length=200)),
                ('cancelledOn', models.DateTimeField(blank=True)),
                ('canceledBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='canceled_by', to=settings.AUTH_USER_MODEL)),
                ('lastModifiedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('requestCreatedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_createdby', to=settings.AUTH_USER_MODEL)),
                ('requestStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='karseva.requeststatus')),
                ('requestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requestor_name', to=settings.AUTH_USER_MODEL)),
                ('subCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='karseva.servicesubcategory')),
                ('userRating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_rating', to='karseva.rating')),
                ('volunteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='volunteer_name', to=settings.AUTH_USER_MODEL)),
                ('volunteerRating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='volunteer_rating', to='karseva.rating')),
            ],
        ),
    ]
