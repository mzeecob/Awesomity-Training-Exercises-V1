from .models import Photo
from django import forms


class ImageForm(forms.ModelForm):
    image_name = forms.CharField()
    image_view = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Photo
        fields = ['image_name', 'image_view']


