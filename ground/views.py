from json.encoder import JSONEncoder
from ground.models import Gig, Image
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):


    return render(request, 'home.html')

def loginorsignup(request):

    return render(request, 'signuporlogin.html')

def view_profile(request, username):
    
    return HttpResponse("THIS IS THE PROFILE PAGE :D")

def creategig(request):
    # print(request.user.profile.is_seller)

    return render(request, 'creategig.html')

def viewgig(request, gig_id):
    RESPONSE = {"ERROR": None, "REQUESTED_GIG": None}

    requested_gigs = len(Gig.objects.filter(id=gig_id))

    if requested_gigs == 0:
        RESPONSE["ERROR"] = "Gig Not Found! :("
    else:
        RESPONSE["REQUESTED_GIG"] = Gig.objects.get(id=gig_id)

    return render(request, 'viewgig.html', RESPONSE)

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

