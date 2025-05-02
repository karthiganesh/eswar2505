from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} in {self.month}"