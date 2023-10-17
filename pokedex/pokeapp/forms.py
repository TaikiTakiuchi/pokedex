from django import forms
from .models import UploadImage
from django.db import models

class UploadForm(forms.ModelForm):
    image=models.ImageField(upload_to='img/')
    class Meta:
        model = UploadImage
        fields = ['image',]
        labels={'image':'画像はこちら'}