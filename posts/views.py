from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Posts


def index(request):
  # return HttpResponse('HELLO FROM POSTS') # Return an HttpResponse instead
  # of a Jinja render function

  posts = Posts.objects.all()[:10]  # get objects from the model
  context = {  # this is passed to render(), similar to props in React
      'title': 'Latest Posts',
      'posts': posts
  }

  return render(request, 'posts/index.html', context)  # pass th


def details(request, id):
  post = Posts.objects.get(id=id)
  context = {
      # map the post object from the Posts model with correct id
      'post': post
  }

  return render(request, 'posts/details.html', context)
