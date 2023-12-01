from django.urls import path
from categories import views

urlpatterns = [

    path('categories/<int:pk>/', views.CategoryDetail.as_view()),

]