from ground.models import Image
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):


    return render(request, 'home.html')

def loginorsignup(request):

    return render(request, 'signuporlogin.html')


# APIs

def checkifusernameexists(request):
    pass

def handlesignup(request):
    pass

def handlelogin(request):
    pass

def handlelogout(request):
    pass

