from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title