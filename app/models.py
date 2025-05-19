from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    background_color = models.CharField(max_length=7, blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    images = models.JSONField(blank=True, default=list)

    def __str__(self):
        return self.name