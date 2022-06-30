from tkinter import CASCADE
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


class Tag(models.Model):
    caption = models.CharField(max_length=1000)


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.CharField(max_length=100)
    content = models.CharField(max_length=1000000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
