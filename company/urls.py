from django.urls import path
from company import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),

]
