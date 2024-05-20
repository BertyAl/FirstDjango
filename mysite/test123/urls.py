from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("shop-detail.html", views.index, name="shop_detail"),
    path("shop-listing.html", views.index, name="shop_listing"),
    path("binpacking.html", views.genetic, name="binpacking"),
]