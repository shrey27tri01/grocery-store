from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class GroceryItem(models.Model):
    STATUS_OPTIONS = (
        ('BOUGHT', 'BOUGHT'),
        ('PENDING', 'PENDING'),
        ('NOT AVAILABLE', 'NOT AVAILABLE')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="groceryitems")
    name = models.TextField(null=True)
    amount = models.TextField(null=True)
    status = models.TextField(max_length=50, choices=STATUS_OPTIONS, default="PENDING")
    date = models.DateField()

    def __str__(self):
        return f"{self.name}"
