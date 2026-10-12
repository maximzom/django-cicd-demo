from django.conf import settings


def app_meta(request):
    return {"app_version": settings.APP_VERSION}
