from django.urls import path
from portfolio import views
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', views.Index, name='index'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('projects/', views.projects, name='projects'),
]
