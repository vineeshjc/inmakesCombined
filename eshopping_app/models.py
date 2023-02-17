from django.db import models
from django.urls import reverse


class categories_db(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='cat_pics')

    class meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('e-shopping:cat_pro', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class products_db(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='pro_pics')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    stock = models.IntegerField(default='0')
    available = models.BooleanField(default=False)
    entered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(categories_db, on_delete=models.CASCADE)

    class meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'


    def get_url(self):
        return reverse('e-shopping:eshop_products', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
