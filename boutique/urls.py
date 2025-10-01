from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('categories/', views.categories, name="categories"),
    path('contact/', views.contact, name="contact"),
]
