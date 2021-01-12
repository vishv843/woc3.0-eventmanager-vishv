from django.db import models

class product(models.Model):
    name = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 2083)
    cost = models.IntegerField()

class offer(models.Model):
    code = models.TextField()
    description = models.TextField()
    discount = models.FloatField()
