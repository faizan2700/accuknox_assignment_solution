from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

class LogEntry(models.Model):
    message = models.TextField()
    thread_id = models.BigIntegerField()