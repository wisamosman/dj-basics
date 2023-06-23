from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm
from django.views import generic

# Create your views here.


class PostList(generic.ListView):
        model = Post


class PostDetail(generic.DetailView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = ['title','publish_date','content','author','image','tags']
    success_url = '/blog/'

class PostEdit(generic.UpdateView):
    model = Post
    fields = ['title','publish_date','content','author','image','tags']
    success_url = '/blog/'
    template_name = 'posts/edit.html'


 
class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/blog/'    





