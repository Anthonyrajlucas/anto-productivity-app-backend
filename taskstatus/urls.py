"""
A module for urls in the taskstatus app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from taskstatus import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('taskstatus/', views.TaskStatusList.as_view()),
    path('taskstatus/<int:pk>/', views.TaskStatusDetail.as_view()),
]