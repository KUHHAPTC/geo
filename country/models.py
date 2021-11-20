from django.db import models

from continent.models import Continent


class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    area = models.DecimalField(max_digits=9, decimal_places=2)
    population = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return f"Country {self.title}"
