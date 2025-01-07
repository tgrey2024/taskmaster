from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'taskmaster'

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.created_at)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
