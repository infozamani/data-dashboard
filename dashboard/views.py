from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
from .models import Dataset
from .forms import ExcelUploadForm

@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            
            # تبدیل به لیست دیکشنری
            data_list = df.to_dict('records')
            column_names = list(df.columns)
            
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.column_names = column_names
            dataset.data = data_list
            dataset.save()
            
            messages.success(request, 'دیتاست با موفقیت ذخیره شد')
            return redirect('dataset_list')
    else:
        form = ExcelUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def dataset_list(request):
    datasets = Dataset.objects.filter(user=request.user)
    return render(request, 'dataset_list.html', {'datasets': datasets})

def api_setup(request):
    return render(request, 'api_setup.html')