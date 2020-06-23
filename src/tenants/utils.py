from tenants.models import Tenant


def tenant_from_request(request):
    host = request.META.get('HTTP_HOST', None)
    if not host:
        raise Exception('Unidentified tenant')
    prefix = host.split('.')[0]
    return Tenant.objects.get(subdomain_prefix=prefix)
