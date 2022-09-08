from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.see_contact, name='see_contact'),
    path('register/', views.register, name='register'),
    path('familiar/', views.see_family, name='see_family'),
    # path('friends/', views.see_friends, name='see_friends'),
    # path('company/', views.see_company, name='see_company'),
]