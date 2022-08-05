# from multiprocessing import context
from django.shortcuts import render
# from django.shortcuts import HttpResponse
from .models import Projects



# Create your views here.
def populate(request):
    """ trying to populate this page """


    # all_project = Projects.objects.all()
    # context = {'items': all_project}

    # return render(request, 'index.html', context)