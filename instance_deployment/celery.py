import django
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instance_deployment.settings')
django.setup()

from instance.helpers.instance_helper import run_commands


app = Celery("instance_deployment")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, max_retries=None)
def run_commands_task(self, instance_id):
    run_commands(instance_id)