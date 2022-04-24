from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return Event.name

class Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(null=True, blank=True, upload_to="media/image")