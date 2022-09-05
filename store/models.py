from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)
    shop = models.ForeignKey(User, on_delete=models.CASCADE)