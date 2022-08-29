from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('html/', views.html_course),
    path('css/', views.css_course),
    path('javascript/', views.javascript_course),
    path('python/', views.python_course),
]
