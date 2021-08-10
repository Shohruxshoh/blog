from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blogapp.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogAppDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogAppCreateVeiw(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogAppUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogAppDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')