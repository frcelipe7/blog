from http.client import HTTPResponse
from django.shortcuts import render
from django.http import request, HttpResponse



def index(request):
    return render(request, 'my_blog/index.html')


def recentes(request):
    return render(request, 'my_blog/recentes.html')
