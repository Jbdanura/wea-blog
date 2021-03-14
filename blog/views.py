from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.
class BlogListView(ListView):
    model = Post
    
class BlogDetailView(DetailView):
    model = Post

class BlogCreateView(CreateView):
    model = Post
    fields = "__all__"

class BlogUpdateView(UpdateView):
    model = Post
    fields = ["title","body"]

class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")