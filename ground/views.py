from json.encoder import JSONEncoder
from ground.models import Gig, Image
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

def home(request):


    return render(request, 'home.html')

def loginorsignup(request):

    return render(request, 'signuporlogin.html')

def view_profile(request, username):
    
    return HttpResponse("THIS IS THE PROFILE PAGE :D")

def creategig(request):
    

    return render(request, 'creategig.html')

def viewgig(request, gig_id):
    RESPONSE = {"ERROR": None, "REQUESTED_GIG": None}

    requested_gigs = len(Gig.objects.filter(id=gig_id))

    if requested_gigs == 0:
        RESPONSE["ERROR"] = "Gig Not Found! :("
    else:
        RESPONSE["REQUESTED_GIG"] = Gig.objects.get(id=gig_id)

        print((Gig.objects.get(id=gig_id).date_of_expiry - Gig.objects.get(id=gig_id).date_created).days)


    RESPONSE["IMAGEE"] = Image.objects.first()

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

def createGigObject(request):
    RESPONSE ={}

    if request.method == 'POST':
        if not request.user.profile.is_seller:
            return JsonResponse({"ERROR": "Erm, you need to be a seller, Mr. Hacker :)"})

        # USER IS SELLER

        title = request.POST['title']
        description = request.POST['description']
        price_per_head = request.POST['price_per_head']
        max_people_count = request.POST['max_people_count']
        date_of_expiry_str = request.POST['date_of_expiry_str']
        gigDuration = request.POST['gigDuration']
        date_of_departure_str = request.POST['date_of_departure']
        destination = request.POST['destination']
        date_of_return_str = request.POST['date_of_return']

        # SERVER SIDE DATA FRISK

        ERRORS = []
        RESPONSE["ERRORS"] = ERRORS
        if len(title) > 150:
            ERRORS.append("Title can't be more than 150 words")

        date_of_expiry = datetime.strptime(date_of_expiry_str, "%Y-%m-%d")
        if (date_of_expiry - datetime.now()).days > 15 and not request.user.profile.is_premium_user:
            ERRORS.append("You need a Premium Account to keep the Gig more than 15 days!")

        date_of_departure = datetime.strptime(date_of_departure_str, "%Y-%m-%d")
        date_of_return = datetime.strptime(date_of_return_str, "%Y-%m-%d")

        if (date_of_departure - datetime.now()).days < 0 or (date_of_return - datetime.now()).days < 0:
            ERRORS.append("We don't have a Time Machine Buddy! Check the Dates of Departure and Return")

        if (date_of_return - date_of_departure).days < 0:
            ERRORS.append("Invalid Return Date")


        print(ERRORS)

        # Return and Terminate if Errors found in Parameter Clutter
        if len(ERRORS) != 0:
            RESPONSE["ERRORS"] = ERRORS
            RESPONSE["ERROR"] = "Submit Request Failed: Inconvinient Data Parameters"
            return JsonResponse(RESPONSE)

        
        # print("HI")

    else:
        return JsonResponse({"ERROR": "Bad Request"})
        
    
    return JsonResponse(RESPONSE)