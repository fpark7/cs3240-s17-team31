from django.contrib import admin
from .models import Report, SiteUser, Group

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    pass
admin.site.register(Report, ReportAdmin)

class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('user','usertype',)


    pass
admin.site.register(SiteUser,SiteUserAdmin)
