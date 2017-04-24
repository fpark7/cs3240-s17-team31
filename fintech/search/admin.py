from django.contrib import admin
from .models import *

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Search, SearchAdmin)

class SearchBarAdmin(admin.ModelAdmin):
    pass
admin.site.register(SearchBar, SearchBarAdmin)
