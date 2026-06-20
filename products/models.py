from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    weight = models.FloatField()

    @property
    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return self.name