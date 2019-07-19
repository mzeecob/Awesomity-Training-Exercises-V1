from .models import Photo
from django import forms


class ImageForm(forms.ModelForm):
    image_name = forms.CharField()
    image_view = forms.ImageField(required=False)

    class Meta:
        model = Photo
        fields = ['image_name', 'image_view']

