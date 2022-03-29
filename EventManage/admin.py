from django.contrib import admin

from EventManage.models import eventregister


class eventregisterAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'mobile', 'course']


admin.site.register(eventregister, eventregisterAdmin)
