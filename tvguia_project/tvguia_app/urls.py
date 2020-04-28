from django.contrib import admin
from django.urls import path, include
from tvguia_app.views import views

app_name = 'tvguia_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('fill/', views.fill, name='fill'),
]
