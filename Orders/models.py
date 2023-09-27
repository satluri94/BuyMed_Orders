from django.db import models
from django.contrib.auth.models import User
import os

class Orders(models.Model):
    orderid = models.CharField(max_length=50, blank=False, default='')
    title = models.CharField(max_length=50, blank=False, default='')
    price = models.CharField(max_length=20, blank=False)
    quantity = models.CharField(max_length=10, blank=False, default='')
    date = models.CharField(max_length=30, blank=False, default='')