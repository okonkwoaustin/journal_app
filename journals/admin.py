from django.contrib import admin
from .models import Journal

class JournalAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "mood", "author", "date_created", "last_updated", "image"]

admin.site.register(Journal, JournalAdmin)
