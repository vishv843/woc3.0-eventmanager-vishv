from django.db import models

class register(models.Model):
    event_name = models.CharField(max_length = 50)
    description = models.TextField()
    poster_link = models.TextField()
    host_id = models.TextField()
