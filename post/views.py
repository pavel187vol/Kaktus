from django.shortcuts import render
from .models import Tag, Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/manage/post/post_list.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/manage/post/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body']
    success_url = '/'
    template_name = 'posts/manage/post/form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = form.instance.title
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'posts/manage/post/form.html'

    def form_valid(self, form):
        form.instance.slug = form.instance.title
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/manage/post/post_confirm_delete.html'
    success_url = '/'
