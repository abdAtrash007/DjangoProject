from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    
class Company(models.Model):
    name = models.TextField()
    
class Category(models.Model):
    catName = models.TextField()
    catDesc = models.TextField()
    