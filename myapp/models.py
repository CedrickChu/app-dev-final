from django.db import models
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Status(BaseModel):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name

class Genre(BaseModel):
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name

class Manga(BaseModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title