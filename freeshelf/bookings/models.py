from django.db import models
from slugify import slugify

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255,)
    author = models.CharField(max_length=100, default=None)
    description = models.TextField(null=True)
    category = models.CharField(max_length=100, default=None, null=True)
    url = models.URLField(max_length=255,)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)

    def save(self):
       if not self.id:
           self.slug = slugify(self.name)
       super(Book, self).save()
