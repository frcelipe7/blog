from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def index(request):
    return render(request, 'my_blog/index.html')


def recentes(request):
    return render(request, 'my_blog/recentes.html')


def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponseRedirect(reverse(index))

    return render(request, 'my_blog/post_view.html', {
        'post': post,
    })
