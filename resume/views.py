from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import random
from .models import Post


def home(request):
    return render(request, 'resume/home.html')


def feedback(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'resume/feedback.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'resume/feedback.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/feedback'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# depricated


def create(request):
    return render(request, 'resume/createaccount.html')
