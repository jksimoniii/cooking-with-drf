
if __name__ == '__main__':
    import django
    django.setup()

from celery.signals import task_failure
from django.conf import settings
from es_common.events import consumer
app = consumer.bus.celery


@app.task
def perform_consume(*args):
    consumer.consume(*args)


@task_failure.connect
def handle_task_failure(**kwargs):
    if hasattr(settings, 'ROLLBAR'):
        import rollbar
        rollbar.report_exc_info(extra_data=kwargs)

