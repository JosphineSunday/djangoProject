from django.db import models

# Create your models here.
class choices(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    summary = models.TextField(blank=True)
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=100)