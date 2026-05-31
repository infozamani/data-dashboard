from django import forms
from .models import Dataset

class ExcelUploadForm(forms.ModelForm):
    excel_file = forms.FileField(label="فایل اکسل")
    
    class Meta:
        model = Dataset
        fields = ['title', 'description']