from django.urls import path
from . import views

urlpatterns = [
  path('users/', views.index),
  path('users/<int:pk>', views.show),
  path('users/<int:pk>/update', views.update),
  path('users/<int:pk>/delete', views.delete),
]
