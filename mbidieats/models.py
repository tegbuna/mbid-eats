from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# returns recipe object based on the slug
    def get_url(self):
        return reverse('details', kwargs={
            'slug':self.slug,
        })
