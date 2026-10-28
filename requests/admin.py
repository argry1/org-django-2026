from django.contrib import admin

from .models import HelpRequest, Application


admin.site.register(HelpRequest)
admin.site.register(Application)