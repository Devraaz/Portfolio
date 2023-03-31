from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("blog", views.blog, name="blog"),
    path("project", views.project, name="project"),

]
