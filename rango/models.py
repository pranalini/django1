from django.db import models
from rango.models import Category
# Create your models here.
class Category(models.Model):
    names = models.CharField(max_length=128, unique=True) #what type
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    class Meta:
        verbous_name_plural = 'Catagories'
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.title
