from email.mime import image
from hashlib import blake2s
import imp
from django.db import models
from django.forms import DateField, SlugField
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='image_blog/')
    tags= TaggableManager()
    author = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now =True)
    prepopulated_fields = {"slug": ("title",)}
    slug= models.SlugField(max_length=200, null=True, blank=True, unique= True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

        
        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return f'{self.title} {self.slug}'



class Contacto(models.Model):
    name = models.CharField(max_length=200,null=False, blank=False)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.name} {self.email}'