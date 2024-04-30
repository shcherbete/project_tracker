from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/new/', views.add_bug, name='add_bug'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/', views.feature_list, name='feature_list'),
    path('features/new/', views.add_feature, name='add_feature'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]