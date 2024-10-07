from django.urls import path
from rest_framework.routers import DefaultRouter
from todolist.apps import TodolistConfig
from todolist.views import *


router = DefaultRouter()


app_name = TodolistConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('about/', about, name='about'),
    # Маршрутизация для работы контроллеров модели Task
    path('tasks/create/', TasktCreateView.as_view(), name='task-create'),
    path('tasks/', TasktListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrievView.as_view(), name='task-retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDestroyView.as_view(), name='task-destroy'),

    # Маршрутизация для работы контроллеров модели Comment
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrievView.as_view(), name='comment-retrieve'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),

    # Маршрутизация для работы контроллеров модели Tag
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/', TagtListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagRetrievView.as_view(), name='tag-retrieve'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDestroyView.as_view(), name='tag-destroy'),

    path('check_deadlines/', check_deadlines, name='check'),
] 
# + router.urls