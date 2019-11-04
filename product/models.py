from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    PRODUCT_STATUS = [
        ('A', 'Available'),
        ('NA', 'Not Available'),
        ('FL', 'Few Left')
    ]
    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=PRODUCT_STATUS)
    created_at = models.DateTimeField(auto_now=True)
