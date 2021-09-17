from django.shortcuts import render
from . models import contact
from django.http import HttpResponse
# Create your views here.
def home(request):

 return render(request,"home/index.html")

def contactUs(request):
    return render(request,"home\contactus.html")


def contactSubmit(request):
    email = request.POST.get("email")
    name = request.POST.get("name")
    tel = request.POST.get("phone")
    desc = request.POST.get("desc")
    File =request.POST.get("screenshot")

    newContact  =  contact(email=email ,name=name , desc=desc , phone=tel ,screenshot=File)
    newContact.save()

    return HttpResponse("Your response has been recorded.")