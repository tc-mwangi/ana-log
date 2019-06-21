from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=40)