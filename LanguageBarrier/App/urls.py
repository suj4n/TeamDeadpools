from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home,name = 'home'),
    path('map/', views.map, name='map'),
    path('currency/', views.currency, name='currency'),
    path('blog/', views.blog, name='blog'), 
    path('blog/update/<int:pk>/', views.updatePost, name='update_post'),
    path('blog/delete/<int:pk>/', views.deletePost, name='delete_post'), 
    path('translate/', views.translate, name='translate'),
    path('weather/', views.weather, name = 'weather'),
    path('places/',views.places,name = 'places'),
    path('places/guides.html', views.guides),
    path('about/', views.about, name = 'about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
