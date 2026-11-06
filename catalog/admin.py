from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Position, Developer, Project, Task


@admin.register(Developer)
class DeveloperAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )


admin.site.register(Position)
admin.site.register(Project)
admin.site.register(Task)
