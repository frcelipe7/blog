from django.shortcuts import render
from django.http import request, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .choices import CATEGORY_CHOICES

from markdown2 import Markdown


def index(request):
    return render(request, 'my_blog/index.html', {
        'posts_recentes': Post.objects.order_by('-id')[:4]
    })


def posts(request):
    return render(request, 'my_blog/recentes.html', {
        'posts_recentes': Post.objects.order_by('-id')
    })


def post_view(request, post_id):
    last_three = Post.objects.order_by('-id')[:3]
    try:
        post = Post.objects.get(id=post_id)
        mkdw = Markdown()
        text = mkdw.convert(post.text)
    except:
        return HttpResponseRedirect(reverse(index))

    return render(request, 'my_blog/post_view.html', {
        'post': post,
        'text': text,
        'last_three': last_three
    })


def categorias(request):
    all_posts = Post.objects.order_by('-id')

    count = 0
    posts_list = []

    for category in CATEGORY_CHOICES:
        count = 0
        for post in all_posts:
            if post.category == category[0]:
                if count < 4:
                    posts_list.append(post)
                    count += 1

    return render(request, 'my_blog/categorias.html', {
        'all_categories': CATEGORY_CHOICES,
        'all_posts': posts_list
    })


def categoria(request, categoria):
    posts_categoria = []
    selected_category = "None"
    for cate in CATEGORY_CHOICES:
        if cate[0].lower() == categoria.lower():
            posts_categoria = Post.objects.filter(category=f"{cate[0]}").order_by('-id')
            selected_category = cate[1].title()
            break
    return render(request, "my_blog/categoria.html", {
        'categoria': selected_category,
        'posts': posts_categoria
    })


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        text = request.POST['text']
        category = request.POST['category']

        post = Post(title=title, image=image, text=text, category=category)

        try:
            post.save()
            return render(request, "my_blog/add.html", {
                'ok_message': "Post enviado com sucesso!"
            })
        except:
            return render(request, "my_blog/add.html", {
                'error_message': "Ocorreu um erro!"
            })
        
    return render(request, 'my_blog/add.html')
