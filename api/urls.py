from django.urls import path

from . import views

urlpatterns = [
  path('problem-1/', views.first_problem, name='first_problem'),
  path('problem-2/', views.second_problem, name='second_problem'),
  path('problem-3/', views.third_problem, name='third_problem'),
]