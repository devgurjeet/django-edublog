from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Posts

def home(request):
    featured = Posts.objects.filter(featured=True, publish=True).order_by('-id').first()
    posts = Posts.objects.filter(featured=False, publish=True).order_by('-id')[:5]

    print(featured)

    context = {
        'featured': featured,
        'posts': posts
    }
    return render(request, 'posts/home.html', context)


def list(request):
    posts = Posts.objects.filter(featured=False, publish=True).order_by('-id')

    context = {
        'posts': posts
    }
    return render(request, 'posts/list.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)
