from django import forms
from .models import *

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_by','created_at','updated_by','updated_at')