from rest_framework import serializers, views, response
from todolist.models import Task, Comment, Tag


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['name', 'description', 'task_date', 'is_done', 'comments', 'tags']
