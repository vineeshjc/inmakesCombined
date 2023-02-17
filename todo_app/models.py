from django.db import models


class todo_db(models.Model):
    name = models.CharField(max_length=250)
    level = models.IntegerField()
    created = models.DateField()

    def __str__(self):
        return self.name

