from django.shortcuts import render
from django.http import request, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .choices import CATEGORY_CHOICES


def index(request):
    return render(request, 'my_blog/index.html', {
        'posts_recentes': Post.objects.order_by('-id')
    })


def posts(request):
    return render(request, 'my_blog/recentes.html', {
        'posts_recentes': Post.objects.order_by('-id')
    })


def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponseRedirect(reverse(index))

    return render(request, 'my_blog/post_view.html', {
        'post': post,
    })


def categorias(request):
    all_posts = Post.objects.order_by('-id')
    return render(request, 'my_blog/categorias.html', {
        'all_categories': CATEGORY_CHOICES,
        'all_posts': all_posts
    })


def categoria(request, categoria):
    for cate in CATEGORY_CHOICES:
        if cate[1].lower() == categoria.lower():
            posts_categoria = Post.objects.filter(category=cate[0])
    return render(request, "my_blog/categoria.html", {
        'posts': posts_categoria
    })
