from django.urls import path

from . import views

urlpatterns = [
  path('problem-1/', views.first_problem, name='first_problem'),
]