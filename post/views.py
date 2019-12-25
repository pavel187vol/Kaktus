from django.shortcuts import render
from .models import Tag, Post
from django.views.generic.list import ListView

class PostListView(ListView):
    model = Post
    template_name = 'posts/manage/post/post_list.html'
