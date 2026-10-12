from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def health(request):
    """Ендпоінт для перевірки, що контейнер живий (healthcheck / smoke-тест)."""
    return JsonResponse({"status": "ok", "version": settings.APP_VERSION})
