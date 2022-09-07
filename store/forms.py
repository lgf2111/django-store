from django import forms
from .models import ProductImage


class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = ProductImage
        fields = ['image']