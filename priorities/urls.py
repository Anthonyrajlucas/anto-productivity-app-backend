from django.urls import path
from priorities import views

urlpatterns = [
    path('priorities/', views.PriorityList.as_view()),
]