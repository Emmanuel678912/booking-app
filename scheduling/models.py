from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
