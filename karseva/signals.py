from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import ServiceRequest,TaskActivity
import datetime
@receiver(pre_save, sender=ServiceRequest)
def my_callback(sender, instance, **kwargs):
    if instance.pk:
        old_instance= ServiceRequest.objects.get(pk=instance.pk)
        if old_instance.volunteer != instance.volunteer:
            TaskActivity.objects.create(service_request=instance,activity_type='VOLUNTEER CHANGE',comments=f'Volunteer --> "{instance.volunteer.first_name}" ')
        if old_instance.requestStatus != instance.requestStatus:
            TaskActivity.objects.create(service_request=instance,activity_type='STATUS CHANGE',comments=f'Status: {old_instance.requestStatus.statusName} --> {instance.requestStatus.statusName}')
        if old_instance.requestTimeInBound != instance.requestTimeInBound or old_instance.requestTimeOutBound != instance.requestTimeOutBound:
            try:
                TaskActivity.objects.create(service_request=instance,activity_type='TIME CHANGE',comments=f'''Time: {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{old_instance.requestTimeInBound}', '%Y-%m-%d %H:%M:%S%z'))} - {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{old_instance.requestTimeOutBound}', '%Y-%m-%d %H:%M:%S%z'))} --> {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{instance.requestTimeInBound}', '%Y-%m-%d %H:%M:%S%z'))} - {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{instance.requestTimeOutBound}', '%Y-%m-%d %H:%M:%S%z'))}''')
            except Exception as e:
                # TaskActivity.objects.create(service_request=instance,activity_type='TIME CHANGE',comments=f'''Time: {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{instance.requestTimeInBound}', '%Y-%m-%d %H:%M:%S%z'))} - {(lambda x: x.strftime("%d %b %y %H:%M"))(datetime.datetime.strptime(f'{instance.requestTimeOutBound}', '%Y-%m-%d %H:%M:%S%z'))}''')
                pass