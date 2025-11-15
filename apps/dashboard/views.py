from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from apps.news.models import News
from datetime import timedelta
from django.db.models import Count


@login_required
def index(request):
    # --- DATA
    total_news = News.objects.count()
    total_users = User.objects.count()

    news_published = News.objects.filter(status="published").count()
    news_draft = News.objects.filter(status="draft").count()

    # User aktif (7 hari)
    active_users = User.objects.filter(
        last_login__gte=timezone.now() - timedelta(days=7)
    ).count()

    # Statistik berita per tanggal (gunakan published_at)
    last_7_days = (
        News.objects
        .filter(published_at__gte=timezone.now() - timedelta(days=7))
        .values("published_at__date")
        .annotate(total=Count("id"))
        .order_by("published_at__date")
    )

    labels = [item["published_at__date"].strftime("%d-%m") for item in last_7_days]
    values = [item["total"] for item in last_7_days]

    # Berita terbaru (gunakan published_at)
    latest_news = News.objects.order_by("-published_at")[:5]

    latest_users = User.objects.order_by("-date_joined")[:5]

    return render(request, "dashboard/index.html", {
        "total_news": total_news,
        "total_users": total_users,
        "news_published": news_published,
        "news_draft": news_draft,
        "active_users": active_users,
        "chart_labels": labels,
        "chart_values": values,
        "latest_news": latest_news,
        "latest_users": latest_users,
    })
