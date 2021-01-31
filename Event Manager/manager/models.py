from django.db import models

class event(models.Model):
    event_ID = models.IntegerField()
    event_name = models.CharField(max_length = 50)
    description = models.TextField()
    from_date = models.DateField()
    from_time = models.TimeField()
    to_date = models.DateField()
    to_time = models.TimeField()
    registration_deadline = models.DateField()
    poster_link = models.TextField()
    password = models.CharField(max_length = 50)
    email_ID = models.EmailField()

class participant(models.Model):
    participant_ID = models.IntegerField()
    name = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 15)
    email_ID = models.EmailField()
    event_name = models.CharField(max_length = 50)
    registration_type = models.CharField(max_length = 20)
    number_of_participants = models.PositiveIntegerField(null = True)

 