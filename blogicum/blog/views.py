"""Rendering blog pages."""
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
from blog.forms import UserForm
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()
posts_on_page = 5
user_model = get_user_model()


def post_filter(
        **kwargs):
    context = {
        'pub_date__lt': datetime.now(),
        'is_published': True,
    }
    context.update(kwargs)
    result = Post.objects.filter(
        **context
    )
    return result


def index(request):
    """Index page with all posts in short view."""
    template_name = 'blog/index.html'
    post_list = post_filter(
        category__is_published=True
    )[:posts_on_page]
    context = {
        'page_obj': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    """Detailed post."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True,
        pk=id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Page with category texts."""
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = post_filter(
        category__slug=category_slug
    )
    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template_name, context)


def profile(request, name):
    """Get user's page."""
    template_name = 'blog/profile.html'
    profile = get_object_or_404(User, username=name)
    page_obj = Post.objects.filter(author__username=name)
    context = {
        'profile': profile,
        'page_obj': page_obj,
    }

    return render(request, template_name, context)


def edit_profile(request):
    template_name = 'blog/user.html'
    # instance = get_object_or_404(User)
    form = UserForm(request.GET or None)  # request.POST or None, instance=instance
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template_name, context)


def create_post(request):
    """Create post by user."""
    template_name = 'blog/create.html'
    return render(request, template_name)
