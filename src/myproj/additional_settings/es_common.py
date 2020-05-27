import os

# Configure Expandshare Bus
ES_BUS_SETTINGS = {
    'backend_model': 'es_common.bus.backends.amqp.AmqpBackend',
    'amqp': {
        'username': os.environ.get('AMQP_USERNAME', 'guest'),
        'password': os.environ.get('AMQP_PASSWORD', 'guest'),
        'host': os.environ.get('AMQP_HOST', 'rabbitmq'),
        'vhost': os.environ.get('AMQP_VHOST', 'local'),
        'queue': 'myproj',
    },
    'app_id': 'myproj'
}
