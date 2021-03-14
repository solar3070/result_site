from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin, ImportMixin

from .models import Result

# Register your models here.

class ResultAdmin(ImportMixin, admin.ModelAdmin):
    pass

admin.site.register(Result, ResultAdmin)