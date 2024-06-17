"""Rendering blog pages."""
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from blog.models import Category, Comment, Post
from blog.forms import CommentForm, UserForm, PostForm
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
    )  # [:posts_on_page]
    posts = post_list.order_by('id')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def post_detail(request, pk):
    """Detailed post."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True,
        pk=pk
    )
    form = CommentForm(request.POST)
    comment = Comment.objects.filter(post__pk=pk).order_by('created_at')
    context = {
        'post': post,
        'user': request.user,
        'form': form,
        'comments': comment,
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
    ).order_by('id')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def profile(request, name):
    """Get user's page."""
    template_name = 'blog/profile.html'
    profile = get_object_or_404(User, username=name)
    posts = Post.objects.filter(author__username=name).order_by('id')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'profile': profile,
        'page_obj': page_obj,
    }

    return render(request, template_name, context)


def edit_profile(request):
    template_name = 'blog/user.html'
    instance = get_object_or_404(User, id=request.user.id)
    form = UserForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template_name, context)

@login_required
def create_post(request, pk=None):
    """Create post by user."""
    template_name = 'blog/create.html'
    if pk is not None:
        instance = get_object_or_404(Post, pk=pk)
    else:
        instance = None
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('blog:profile', name=request.user)
    return render(request, template_name, context)


def edit_post(request, pk):
    """Edit post, authered by user."""
    template_name = 'blog/create.html'
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('blog:post_detail', id=pk)

    return render(request, template_name, context)


def delete_post(request, pk):
    """Delete post if user is author."""
    template_name = 'blog/create.html'
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('blog:profile', name=request.user)        
    return render(request, template_name, context)


@login_required
def add_comment(request, pk):
    """Comment post by authenticated user."""
    # Получаем объект дня рождения или выбрасываем 404 ошибку.
    post = get_object_or_404(Post, pk=pk)
    # Функция должна обрабатывать только POST-запросы.
    form = CommentForm(request.POST)
    if form.is_valid():
        # Создаём объект поздравления, но не сохраняем его в БД.
        comment = form.save(commit=False)
        # В поле author передаём объект автора поздравления.
        comment.author = request.user
        # В поле birthday передаём объект дня рождения.
        comment.post = post
        # Сохраняем объект в БД.
        comment.save()
    # Перенаправляем пользователя назад, на страницу дня рождения.
    return redirect('blog:post_detail', pk=pk) 


def edit_comment(request, pk, id):
    """Edit post by it's author."""
    pass


def delete_comment(request, pk, id):
    """Delete post - user is author."""
    pass


'''
  template_name = 'blog/comment.html'
    if pk is not None:
        instance = get_object_or_404(Comment, pk=pk)
    else:
        instance = None
    form = CommentForm(
        request.POST or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('blog:profile', name=request.user)
    return render(request, template_name, context)
'''