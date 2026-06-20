from django.db import models


class Box(models.Model):
    name = models.CharField(max_length=100)

    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    max_weight = models.FloatField()

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    @property
    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return self.name