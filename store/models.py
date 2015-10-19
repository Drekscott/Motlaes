from django.db import models

# Create your models here.
sizes = (('S','Small'),('M','Medium'),('L','Large'),('XL','Extra Large'), ('XXL','2X Large'))

class About(models.Model):
    about_pic = models.ImageField()
    about_name = models.CharField(max_length=120)
    about_txt = models.TextField(blank=True)
    
class Categories(models.Model):
    category_name = models.CharField(max_length=120)
    
class Items(models.Model):
    category = models.ForeignKey(Categories)
    item_name = models.CharField(max_length=120)
    price = models.FloatField()
    item_image = models.ImageField()
    item_sizes = models.CharField(choices=sizes, max_length=10)
    