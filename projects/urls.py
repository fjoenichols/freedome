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
    path('project/<pk>/confirm', views.project_confirm_delete, name='project_confirm_delete'),
    path('project/<pk>/delete', views.project_delete, name='project_delete'),
    path('project/<pk>/update', views.project_update, name='project_update'),
    path('task/<pk>/confirm', views.task_confirm_delete, name='task_confirm_delete'),
    path('task/<pk>/delete', views.task_delete, name='task_delete'),
    path('task/<pk>/update', views.task_update, name='task_update'),
    path('subtask/<pk>/confirm', views.subtask_confirm_delete, name='subtask_confirm_delete'),
    path('subtask/<pk>/delete', views.subtask_delete, name='subtask_delete'),
    path('subtask/<pk>/update', views.subtask_update, name='subtask_update'),

]