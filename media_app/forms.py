from django import forms
from .models import Media
from django.core.exceptions import ValidationError

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ('name', 'description', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter file write-up', 'rows': 4}),
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            # Check if it's a new upload (has content_type) or existing file (FieldFile)
            if hasattr(file, 'content_type'):
                content_type = file.content_type.split('/')[0]
                if content_type not in ['image', 'video']:
                    raise ValidationError("File type is not supported. Please upload an image or video file.")
        return file
