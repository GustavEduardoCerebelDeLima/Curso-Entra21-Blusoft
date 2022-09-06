from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.see_contact, name='see_contact'),
    path('<int:contact_category>', views.see_family, name='see_family'),
    path('<int:contact_category>', views.see_friends, name='see_friends'),
    path('<int:contact_category>', views.see_company, name='see_company'),
]