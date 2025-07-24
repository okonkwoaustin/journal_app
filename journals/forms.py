from django import forms
from .models import Journal

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'content', 'mood', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'mood': forms.Select(attrs={'class': 'form-select'}),
        }