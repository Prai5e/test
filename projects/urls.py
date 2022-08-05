from django.urls import path

# from theModels.views import populate
from . import views


urlpatterns = [
    path("",views.home,name="index"),
    path("",views.index1,name="index1"),
    path("index1",views.index1,name="index1"),
    path('index', views.index, name='index'),
    path('index/populate', views.populate, name='populate')
]
