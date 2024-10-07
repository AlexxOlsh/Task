from django.shortcuts import render
from django.core.cache import cache
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from todolist.models import Task, Comment, Tag
from todolist.serializers import TaskSerializer, CommentSerializer, TagSerializer
from rest_framework.permissions import BasePermission
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .task import check_comment_for_bad_words, check_tasks_deadlines


def check_deadlines(request):
    check_tasks_deadlines.delay()
    return HttpResponse("Task triggered")


AUTH_MODE = [IsAuthenticated]


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Create your views here.
def base(request):
    return render(request, "todolist/base.html", context={'base':'Base info'})


def about(request):
    return render(request, "todolist/about.html")


class TasktCreateView(generics.CreateAPIView):
    ''' Класс-контроллер для создани объектов модели Task '''
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TasktListView(generics.ListAPIView):
    ''' Класс-контроллер для просмотра списка объектов модели Task '''
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Task '''
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Task '''
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Task '''
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Comment Views
class CommentCreateView(generics.CreateAPIView):
    ''' Класс-контроллер для создани объектов модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment = serializer.save()
        check_comment_for_bad_words.delay(comment.id)


class CommentListView(generics.ListAPIView):
    ''' Класс-контроллер для просомтра списка объектов модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Tag Views
class TagCreateView(generics.CreateAPIView):
    ''' Класс-контроллер для создани объектов модели Tag '''
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagtListView(generics.ListAPIView):
    ''' Класс-контроллер для просомтра списка объектов модели Tag '''
    permission_classes = AUTH_MODE
    tags_cache_name = 'tags_cache'
    tags_cache = cache.get(tags_cache_name)

    if tags_cache:
        queryset = tags_cache
    else:
        queryset = Tag.objects.all()
        cache.set(tags_cache_name, queryset, 30)

    serializer_class = TagSerializer


class TagRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Tag '''
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Tag '''
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Comment '''
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer