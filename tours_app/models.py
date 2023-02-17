from django.db import models


class header_back(models.Model):
    name = models.CharField(max_length=250, default='Header Background')
    image = models.ImageField(upload_to='header_background')

    def __str__(self):
        return self.name


class footer_back(models.Model):
    name = models.CharField(max_length=250, default='Footer Background', blank=True)
    image = models.ImageField(upload_to='footer_background')

    def __str__(self):
        return self.name


class banner_back(models.Model):
    name = models.CharField(max_length=250, default='Banner Background', blank=True)
    image = models.ImageField(upload_to='banner_background')

    def __str__(self):
        return self.name


class our_team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Our_team_images')
    detail = models.TextField()

    def __str__(self):
        return self.name


class our_tours(models.Model):
    name = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='Our_tours_images')
    detail = models.TextField(blank=True)

    def __str__(self):
        return self.name
