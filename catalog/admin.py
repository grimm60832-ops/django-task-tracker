from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Developer, Task, Position, Project, TaskComment


@admin.register(Developer)
class DeveloperAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ("task", "author", "created_at", "comment")  # какие поля показывать в таблице
    list_filter = ("created_at", "author")                     # фильтры справа в админке
    search_fields = ("comment", "author__username")


admin.site.register(Position)
admin.site.register(Project)
admin.site.register(Task)
