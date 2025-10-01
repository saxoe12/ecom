from django.db import models

# Create your models here.
class Produit(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=200)
    lien_affiliation = models.URLField(max_length=200)
    categorie = models.CharField(max_length=100, blank=True, null=True)

   

    def __str__(self):
        return self.titre