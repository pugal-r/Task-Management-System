from django.db import models

class TaskModel(models.Model):
    user_id = models.IntegerField(null=True, blank=True)  # ✅ plain integer, no ForeignKey
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)