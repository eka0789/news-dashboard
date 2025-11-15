from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import News, Category


# LIST
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, "news/category_list.html", {"categories": categories})


# CREATE
@login_required
def category_create(request):
    if request.method == "POST":
        name = request.POST.get("name")

        # Validasi sederhana
        if Category.objects.filter(name=name).exists():
            messages.error(request, "Kategori sudah ada.")
            return redirect("category.create")

        Category.objects.create(name=name)
        messages.success(request, "Kategori berhasil ditambahkan.")
        return redirect("category.index")

    return render(request, "news/category_create.html")


# EDIT
@login_required
def category_edit(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        name = request.POST.get("name")

        # Cek duplikasi nama kategori lain
        if Category.objects.filter(name=name).exclude(id=id).exists():
            messages.error(request, "Kategori dengan nama tersebut sudah ada.")
            return redirect("category.edit", id=id)

        category.name = name
        category.save()

        messages.success(request, "Kategori berhasil diperbarui.")
        return redirect("category.index")

    return render(request, "news/category_edit.html", {"category": category})


# DELETE
@login_required
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()

    messages.success(request, "Kategori berhasil dihapus.")
    return redirect("category.index")

# LIST
@login_required
def news_list(request):
    news = News.objects.select_related('category', 'author').all().order_by('-id')
    return render(request, "news/news_list.html", {"news": news})


# CREATE
@login_required
def news_create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")
        status = request.POST.get("status")
        thumbnail = request.FILES.get("thumbnail")

        category = Category.objects.get(id=category_id)

        News.objects.create(
            title=title,
            content=content,
            category=category,
            status=status,
            thumbnail=thumbnail,
            author=request.user
        )

        messages.success(request, "Berita berhasil ditambahkan.")
        return redirect("news.index")

    return render(request, "news/news_create.html", {
        "categories": categories
    })


# EDIT
@login_required
def news_edit(request, id):
    news = get_object_or_404(News, id=id)
    categories = Category.objects.all()

    if request.method == "POST":
        news.title = request.POST.get("title")
        news.content = request.POST.get("content")
        news.status = request.POST.get("status")
        news.category_id = request.POST.get("category")

        if request.FILES.get("thumbnail"):
            news.thumbnail = request.FILES.get("thumbnail")

        news.save()

        messages.success(request, "Berita berhasil diperbarui.")
        return redirect("news.index")

    return render(request, "news/news_edit.html", {
        "news": news,
        "categories": categories
    })


# DELETE
@login_required
def news_delete(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()

    messages.success(request, "Berita berhasil dihapus.")
    return redirect("news.index")
