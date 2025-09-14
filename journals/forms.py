from django import forms
from .models import Journal
from taggit.forms import TagWidget


class JournalEntryForm(forms.ModelForm):    
    class Meta:
        model = Journal
        fields = ["title", "content", "mood", "tags", "is_private", "image",]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "mood": forms.Select(attrs={"class": "form-select"}),
            "tags": TagWidget(attrs={"class": "form-control", "placeholder": "e.g. reflection, gratitude"}),
        }
