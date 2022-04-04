from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='resume-home'),
    path('feedback', views.feedback, name='feedback'),
    path('create', views.create, name='create-account'),
]
