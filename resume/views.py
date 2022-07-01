from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Post


def home(request):
    return render(request, 'resume/home.html')


def feedback(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'resume/feedback.html', context)


def create(request):
    return render(request, 'resume/createaccount.html')
