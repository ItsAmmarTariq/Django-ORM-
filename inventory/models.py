from django.db import models


# Create your models here.

class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    units=models.BigIntegerField()
    product=models.OneToOneField(Product, on_delete=models.CASCADE)




