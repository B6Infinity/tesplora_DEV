from json.encoder import JSONEncoder
from ground.models import Image
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):


    return render(request, 'home.html')

def loginorsignup(request):

    return render(request, 'signuporlogin.html')

def view_profile(request):
    pass

def creategig(request):
    # print(request.user.profile.is_seller)

    return render(request, 'creategig.html')


# APIs

def checkifusernameexists(request):
    if request.method == 'POST':
        RESPONSE = {}

        try:

            username = request.POST['username']
            print(username)
            RESPONSE["username"] = str(username)
            
            if len(User.objects.filter(username=str(username))) == 0: 
                RESPONSE["exists"] = False
            else:
                RESPONSE["exists"] = True

        except Exception:
            RESPONSE = {"ERROR": "Failed! Server Side Error... Broteen k bolo :)"}


    else:
        return JsonResponse({"ERROR": "Bad Request"})
        
    
    return JsonResponse(RESPONSE)

def handlesignup(request):
    pass

def handlelogin(request):
    pass

def handlelogout(request):
    pass

