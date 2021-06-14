from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ExploreHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("productView/", views.prodView, name="ProdView"),
    path("compare/", views.Compare, name="Compare")
]
