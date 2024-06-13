from django.urls import path, include, reverse_lazy

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
    path('profile/<slug:name>/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/edit/', views.edit_post, name="edit_post"),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('posts/<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<int:id>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('posts/<int:id>/delete_comment/', views.delete_comment, name='delete_comment'),
]
