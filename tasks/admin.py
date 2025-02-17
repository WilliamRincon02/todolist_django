from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "priority",
        "completed",
        "created_at"
    )
    search_fields = ["name"]

admin.site.register(Task)