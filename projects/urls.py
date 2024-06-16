from django.urls import path
from . import views

urlpatterns = [
       path('public/projects/', views.project_public, name='project_public'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.project_create, name='project_create'),
    path('project/<pk>', views.project_detail, name='project_detail'),
    path('task/<pk>', views.task_detail, name='task_detail'),
    path('subtask/<pk>', views.subtask_detail, name='subtask_detail'),
    path('project/<pk>/comment/new', views.project_comment, name='project_comment'),
    path('task/<pk>/comment/new', views.task_comment, name='task_comment'),
    path('subtask/<pk>/comment/new', views.subtask_comment, name='subtask_comment'),
]