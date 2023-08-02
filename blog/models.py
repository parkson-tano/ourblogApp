from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    category  = models.ForeignKey('Category', on_delete=models.PROTECT)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
