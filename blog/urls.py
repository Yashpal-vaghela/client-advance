
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.blog_home, name='blog'),
    path('search-in-blogs', views.myblogsearch, name='myblogsearch'),
    path('all-blogs/', views.blog_list, name='blog_list'),
    path('all-blogs/<str:pk>/', views.cat_list, name='cat_list'),
] 
