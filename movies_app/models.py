from django.db import models


class movies_mod(models.Model):
    name = models.CharField(max_length=250)
    story = models.TextField()
    image = models.ImageField(upload_to='movies_pics')
    released = models.IntegerField()
