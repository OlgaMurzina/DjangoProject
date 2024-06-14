from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^about', TemplateView.as_view(template_name='firstapp/about.html'), name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^products/(?P<productid>\d+)/', views.products, name='products'),
    re_path(r'^users/', views.users, name='users'),
    path('access/<int:age>/', views.access, name='access'),
]
