from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recentes', views.recentes, name='recentes'),
    path('posts/post_id=<int:post_id>', views.post_view, name='post_view'),
]
