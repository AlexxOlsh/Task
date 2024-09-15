from datetime import datetime
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    author = models.CharField(max_length=200, null=True, blank=True, verbose_name='Автор')
    description = models.TextField(null=True, verbose_name='Текст задачи')
    task_date = models.DateTimeField(default=datetime.now, null=False, verbose_name='Дата время')
    is_done = models.BooleanField(null=True, verbose_name='Выполнена')
    tags = models.ManyToManyField('Tag', related_name='tasks')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['task_date']
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Comment(models.Model):
    name = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.id} on {self.created_at}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
