from django.shortcuts import render
from rest_framework import generics, viewsets
from todolist.models import Task, Comment, Tag
from todolist.serializers import TaskSerializer, CommentSerializer, TagSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TasktListView(generics.ListAPIView):
    ''' Класс-контроллер для просмотра списка объектов модели Task '''

    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class TaskRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Task '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Task '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Task '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Comment Views
class CommentCreateView(generics.CreateAPIView):
    ''' Класс-контроллер для создани объектов модели Comment '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListView(generics.ListAPIView):
    ''' Класс-контроллер для просомтра списка объектов модели Comment '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Comment '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Comment '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Comment '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Tag Views
class TagCreateView(generics.CreateAPIView):
    ''' Класс-контроллер для создани объектов модели Tag '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagtListView(generics.ListAPIView):
    ''' Класс-контроллер для просомтра списка объектов модели Tag '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrievView(generics.RetrieveAPIView):
    ''' Класс-контроллер для просмотра отдельного объекта модели Tag '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    ''' Класс-контроллер для редактирования объектов модели Tag '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDestroyView(generics.DestroyAPIView):
    ''' Класс-контроллер для удаления объектов модели Comment '''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer