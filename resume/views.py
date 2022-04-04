from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'resume/home.html')


def feedback(request):
    return render(request, 'resume/feedback.html')


def create(request):
    return render(request, 'resume/createaccount.html')
