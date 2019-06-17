from django.db import models
from django.utils.text import slugify

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     category_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     description = models.TextField(blank=True)
#     slug= models.SlugField(blank=True)
#     class Meta:
#         verbose_name_plural = "categories"  
#     def __str__(self):
#         return self.name
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    slug= models.SlugField(blank=True)
    class Meta:
        verbose_name_plural = "categories"  
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)