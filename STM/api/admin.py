from django.contrib import admin
from .models import CustomUser, Task

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['id', 'username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_active', 'groups']
    ordering = ['id']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'due_date']
    search_fields = ['title', 'user__email']
    list_filter = ['status', 'due_date']
    ordering = ['id']
