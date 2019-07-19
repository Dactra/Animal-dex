from django.template.defaultfilters import slugify

from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image_url = models.CharField(max_length=800) # image urls are rly long
    summary = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Animal, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cat(Animal):
    other_names = models.CharField(max_length=400, default=None, blank=True, null=True)
    nicknames = models.CharField(max_length=400, default=None, blank=True, null=True)
    origin = models.CharField(max_length=200, default=None, blank=True, null=True)
    
class Dog(Animal):
    other_names = models.CharField(max_length=400, default=None, blank=True, null=True)
    nicknames = models.CharField(max_length=400, default=None, blank=True, null=True)
    origin = models.CharField(max_length=200, default=None, blank=True, null=True)
    weight = models.CharField(max_length=200, default=None, blank=True, null=True)
    height = models.CharField(max_length=200, default=None, blank=True, null=True)
    coat = models.CharField(max_length=200, default=None, blank=True, null=True)
    color = models.CharField(max_length=200, default=None, blank=True, null=True)
    lifespan = models.CharField(max_length=200, default=None, blank=True, null=True)
    
class Bird(Animal):
    conservation_status = models.CharField(max_length=200, default=None, blank=True, null=True)
    kingdom = models.CharField(max_length=200, default=None, blank=True, null=True)
    phylum = models.CharField(max_length=200, default=None, blank=True, null=True)
    scientific_class = models.CharField(max_length=200, default=None, blank=True, null=True)
    order = models.CharField(max_length=200, default=None, blank=True, null=True)
    family = models.CharField(max_length=200, default=None, blank=True, null=True)
    genus = models.CharField(max_length=200, default=None, blank=True, null=True)
    species = models.CharField(max_length=200, default=None, blank=True, null=True)
    binomial_name = models.CharField(max_length=200, default=None, blank=True, null=True)

