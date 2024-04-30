from django.urls import path, include
from tasks import views
from quality_control import views as qc_views

app_name = 'tasks'

urlpatterns = [
    # path('', views.index),
    # path('another/', views.another_page, name='another_page'),
    # path('quality_control/', views.quality_control, name='quality_control'),
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('another/', views.another_page, name='another_page'),
    path('quality_control/', views.quality_control, name='quality_control'),
    path('projects/', views.ProjectsListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail')
]