from django.urls import path
from company import views

urlpatterns = [
    path('index/', views.index, name='index')

]
