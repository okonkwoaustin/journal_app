from django.contrib import admin
from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "mood",
        "author",
        "image",
        "date_created",
        "last_updated",
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Journal, JournalAdmin)
