from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
