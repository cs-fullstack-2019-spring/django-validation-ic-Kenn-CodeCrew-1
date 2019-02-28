from django.urls import path
from . import views


urlpatterns = [
    path("", views.cocktails, name="cocktail"),
    path("users/", views.index, name="index"),
]