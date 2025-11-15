from django.shortcuts import render, get_object_or_404
from .models import News, Category

def landing_page(request):
    latest_news = News.objects.filter(status="published").order_by('-published_at')[:6]
    hero = News.objects.filter(status="published").order_by('-published_at').first()
    categories = Category.objects.all()

    return render(request, "public/landing.html", {
        "latest_news": latest_news,
        "hero": hero,
        "categories": categories,
    })


def public_detail(request, slug):
    item = get_object_or_404(News, slug=slug, status="published")
    categories = Category.objects.all()

    return render(request, "public/detail.html", {
        "item": item,
        "categories": categories
    })


def public_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category, status="published")

    return render(request, "public/category.html", {
        "news": news,
        "category": category
    })
