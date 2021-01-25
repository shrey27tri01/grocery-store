
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.addListView, name="add"),
    path("edit/<itemId>", views.edit, name="itemEdit"),
    path("delete/<itemId>", views.delete, name="delete"),
    path("filter", views.filter, name="filter")
]
