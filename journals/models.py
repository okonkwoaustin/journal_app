from django.db import models
from django.conf import settings
import uuid
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    pass

#class Tag(models.Model):
#    """Tags to organize journal entries (e.g. 'work', 'travel', 'family')."""
#   name = models.CharField(max_length=50, unique=True)

#    def __str__(self):
#        return self.name

class Journal(models.Model):
    """Main journal entry model with mood tracking and media support."""

    MOOD_CHOICES = [
        ("happy", "Happy"),
        ("sad", "Sad"),
        ("neutral", "Neutral"),
        ("anxious", "Anxious"),
        ("excited", "Excited"),
        ("angry", "Angry"),
        ("grateful", "Grateful"),
        ("motivated", "Motivated"),
        ("reflective", "Reflective"),
        ("inspired", "Inspired"),
        ("stressed", "Stressed"),
        ("calm", "Calm"),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    content = models.TextField()
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default="neutral")
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    tags = TaggableManager(through=UUIDTaggedItem)
    image = models.ImageField(upload_to="journal_images/", blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.date_created.strftime('%b %d, %Y')}"

    class Meta:
        ordering = ["-date_created"]
        get_latest_by = 'date_created' 
