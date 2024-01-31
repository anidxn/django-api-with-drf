from django.contrib import admin
from . import models

class CompanyAdmin(admin.ModelAdmin):
    # layout for table columns in admin login
    list_display = ('name', 'location', 'type', 'company_id')
    # create a search field
    search_fields = ('name', ) # search based on names


class EmployeeAdmin(admin.ModelAdmin):
    # layout for table columns in admin login
    list_display = ('name', 'email', 'position', 'company')
    # filter based on a column
    list_filter = ('company',)

# Register your models here.
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Employee, EmployeeAdmin)