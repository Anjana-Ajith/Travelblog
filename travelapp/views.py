from django.http import HttpResponse
from django.shortcuts import render
from . models import place,blog

# Create your views here.
def fun(request):
    obj=place.objects.all()
    obj1 = blog.objects.all()
    return render(request, "index.html",{'results':obj,'newses':obj1})


def addition(request):
#    num1=int(request.GET["num1"])
 #   num2= int(request.GET["num2"])
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})