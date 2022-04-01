from django.db import models


class Video(models.Model):
    video = models.FileField()
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title