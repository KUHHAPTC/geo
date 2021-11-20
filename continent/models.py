from django.db import models


class Continent(models.Model):
    title = models.CharField(max_length=30, unique=True)
    area = models.PositiveIntegerField()

    def __str__(self):
        return f"Continent {self.title}"
