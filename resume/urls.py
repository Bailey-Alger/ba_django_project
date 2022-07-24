from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='resume-home'),
    path('feedback', views.feedback, name='feedback'),
    path('create', views.create, name='create-account'),
    path('register/', user_views.register, name='register'),
]
