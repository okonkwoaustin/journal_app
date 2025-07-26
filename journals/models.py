from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    """ Journal models a task"""
    MOOD_CHOICES = [
        ("happy", "Happy"),
        ("sad", "Sad"),
        ("neutral", "Neutral"),
        ("anxious", "Anxious"),
        ("excited", "Excited"),
        ("angry", "Angry"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default="neutral")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField("journal_images/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.date_created.strftime('%b %d, %Y')}"

    class Meta:
        ordering = ["-date_created"]