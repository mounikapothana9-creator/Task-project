from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.IntegerField()
    task_name = models.CharField(max_length=30)
    task_start_date = models.DateField()
    task_end_date = models.DateField()
    