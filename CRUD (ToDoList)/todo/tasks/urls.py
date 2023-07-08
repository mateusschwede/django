from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('task/<str:pk>/', views.detailTask, name="detail"),
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]