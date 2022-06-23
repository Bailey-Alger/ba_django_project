from django.shortcuts import render
from django.http import HttpResponse
import random

posts = [
    {
        'author': 'Bailey Alger',
        'title': 'Feedback Post 1',
        'content': 'First post content',
        'date_posted': 'June 23, 2022'
    },
    {
        'author': 'Bob Smith',
        'title': 'Feedback Post 2',
        'content': 'Second post content',
        'date_posted': 'June 23, 2022'
    }
]


def home(request):
    return render(request, 'resume/home.html')


def feedback(request):
    context = {
        'posts': posts
    }
    return render(request, 'resume/feedback.html', context)


def create(request):
    return render(request, 'resume/createaccount.html')
