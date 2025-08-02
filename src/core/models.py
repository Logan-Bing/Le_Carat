from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
