from distutils.command.upload import upload
from email.policy import default
from unicodedata import category
from django.db import models
from .choices import *


class Post(models.Model):
    title = models.CharField(max_length=60, default="Título do post")
    image = models.ImageField(upload_to='posts_images/%m', default='default.jpeg')
    text = models.TextField(default='Área de texto', max_length=2000)
    likes = models.IntegerField(default=0)
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_CHOICES,
        default=TECNOLOGIA
    )


class NewsLetter(models.Model):
    name = models.CharField(max_length=100, default="Usuário")
    email = models.EmailField(default="email@email.com", max_length=100)


all_classes = [
    Post,
    NewsLetter,
]