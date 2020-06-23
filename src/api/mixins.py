from rest_framework.viewsets import ModelViewSet

from tenants.utils import tenant_from_request


class TenantAwareModelViewSet(ModelViewSet):
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
