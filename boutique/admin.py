from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre', 'prix', 'categorie')
    search_fields = ('titre', 'categorie')



