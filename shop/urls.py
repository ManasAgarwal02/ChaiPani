from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path("", views.index, name="ShopIndex"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("preview/", views.preview, name="preview"),
    path("preview/confirm/", views.confirm, name="confirm"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
