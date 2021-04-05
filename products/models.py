from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


admin.site.site_header = "Florescence Administration Dashboard"


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colour = models.ForeignKey(
        'Colour', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey(
        'Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    featured = models.BooleanField(default=False)
    avg_rating = models.FloatField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Colour(models.Model):

    class Meta:
        verbose_name_plural = 'Colours'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Occasion(models.Model):

    class Meta:
        verbose_name_plural = 'Occasions'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductReview(models.Model):

    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000, blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ProductRating(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.PositiveSmallIntegerField()
    review = models.OneToOneField(
        'ProductReview', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
