from django import forms
from .models import Manga

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'img', 'status', 'genre', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        return title