from django.shortcuts import render
from .models import*
import pandas as pd
from django.contrib.auth.models import User,auth
# Create your views here.

def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'index.html', context=mydict)






# # Create your views here.
def index(request):
    return render(request,'index.html')

def index1(request):
    if request.method=='POST':
        # title=request.POST['']       
        upload=request.FILES['file_upload']
        object=Projects.objects.create(name='oversabi',file_upload=upload,)
        object.save()  
    context= excel_data
    return render(request,'index1.html',{'context':context})