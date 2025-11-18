from django.urls import path
from . import views
urlpatterns =[
       path('', views.home, name='home'),
       path('rooms/about/', views.about, name='about'),
       path('rooms/vacancy/', views.vacancy, name='vacancy'),
       path('rooms/contact', views.contact, name='contact'),
]