from django.db import models

class register(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length = 50)
    description = models.TextField()
    from_date = models.CharField(max_length = 50)
    from_time = models.CharField(max_length = 10)
    to_date = models.CharField(max_length = 50)
    to_time = models.CharField(max_length = 10)
    poster_link = models.TextField()
    host_id = models.EmailField()

class participant(models.Model):
    part_id = models.IntegerField()
    part_name = models.CharField(max_length = 50)
    contact = models.IntegerField()
    email_id = models.EmailField()
    event = models.CharField(max_length = 50)
    reg_type = models.CharField(max_length = 20)
    people = models.IntegerField(null = True)

 