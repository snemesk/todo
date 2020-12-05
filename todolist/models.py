from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [(1, '未完了'),(2, '作業中'),(3, '完了')]

    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    due_date =  models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='document/',blank=True,null=True)
 
    def publish(self):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title