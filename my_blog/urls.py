from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('posts/post_id=<int:post_id>', views.post_view, name='post_view'),
    path('categorias', views.categorias, name='categorias'),
    path('categoria/<str:categoria>', views.categoria, name='categoria'),
]
