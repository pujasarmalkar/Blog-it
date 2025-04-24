from django.urls import path
from . import views

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
	path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
	path('<int:pk>/edit/', views.edit_blog, name='edit_blog'),
	path('<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),
    path('unlike/<int:blog_id>/', views.unlike_blog, name='unlike_blog'),
    path('search_result/', views.search_blogs, name='search_blogs'),
    path('', views.homepage, name='homepage'),
]
