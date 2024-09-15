from django.contrib import admin
from todolist.models import Task, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Task)
class Task_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'task_date')
    list_display_links = ('id', 'name')
    ordering = ['task_date', 'id']
    search_fields = ('name', 'description')
    list_filter = ('task_date', 'author')


    inlines = [
        CommentInline,
    ]


# Register your models here.
