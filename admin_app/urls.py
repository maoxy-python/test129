from django.urls import path
from admin_app import views


urlpatterns = [
    path('index/', views.index),
    path('addParentCate/', views.addParentCate),
    path('add/', views.addBook),
]
