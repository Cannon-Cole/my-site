from tkinter import CASCADE
from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.CharField(max_length=100, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)
