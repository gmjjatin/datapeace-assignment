from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from user.models import *

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.register(User,UserAdmin)
