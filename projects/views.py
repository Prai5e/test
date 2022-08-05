from django.shortcuts import render, redirect
from .models import*
import pandas as pd
from django.contrib.auth.models import User,auth
from theModels.models import Projects


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
    return render(request,'index1.html',{})



def populate(request):
    if request.method == 'GET':
        item = Projects.objects.filter(username='Frodo')
        # for i in item:

        # name = item.username
        # project = item.project_name
        # file = item.file_one
        # date = item.date_created
        # lasttime = item.last_modified
        context = {
            'ListBox' : item
        }

        return render(request, 'page.html', context)


    # def index(request):
    #     return render(request,'index.html')