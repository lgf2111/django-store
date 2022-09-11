from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        output_size = (500, 500)
        img.thumbnail(output_size)
        img.save(self.image.path)


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class CartItem(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
