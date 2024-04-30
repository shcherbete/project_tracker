from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list')
]