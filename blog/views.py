from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
import logging

def home(request):
    return render(request, 'index.html')

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'articles': articles, 'categories': categories})

def view_post(request, slug):
    post = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/view_post.html', {'post': post})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_posts = Article.objects.filter(category = category)
    return render(request, 'blog/view_category.html', {'category': category, 'articles': category_posts})