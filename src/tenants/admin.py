from django.contrib import admin

from tenants import models

admin.site.register(models.Tenant)
