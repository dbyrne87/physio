from django.db import models

# Fields of whats needed to add a product #
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    long_description = models.TextField(default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
