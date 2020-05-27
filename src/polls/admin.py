from django.contrib import admin

from polls import models

admin.site.register(models.Choice)
admin.site.register(models.Question)
