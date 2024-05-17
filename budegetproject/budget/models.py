from django.db import models
from django.utils.text import slugify

class project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , unique= True , blank= True)
    budget = models.IntegerField()
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Project , self)
        
    