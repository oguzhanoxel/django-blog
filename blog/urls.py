from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete', views.post_delete, name='post_delete'),
]