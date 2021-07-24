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


    return render(request, 'viewgig.html', RESPONSE)

def editgig(request, gig_id):
    
    RESPONSE = {}
    
    # Check if Gig exists
    _requested_gig = Gig.objects.filter(id=gig_id)
    if len(_requested_gig) == 0:
        RESPONSE["ERROR"] = "Gig Not Found!"
        return render(request, 'editgig.html', RESPONSE)

    requested_gig = _requested_gig[0]
    
    # Check if Request.user is the author
    if request.user != requested_gig.author:
        RESPONSE["ERROR"] = "That's not your Gig, is it?"
        return render(request, 'editgig.html', RESPONSE)

    RESPONSE["REQUESTED_GIG"] = requested_gig

    return render(request, 'editgig.html', RESPONSE)
    


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
    RESPONSE ={"STATUS": "Failed"}

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


        # Return and Terminate if Errors found in Parameter Clutter
        if len(ERRORS) != 0:
            RESPONSE["ERRORS"] = ERRORS
            RESPONSE["ERROR"] = "Submit Request Failed: Inconvinient Data Parameters"
            return JsonResponse(RESPONSE)


        # Create Gig Object

        new_Gig = Gig.objects.create(
            title = title,
            destination = destination,
            author = request.user,
            description = description,
            price = price_per_head,
            date_of_expiry = date_of_expiry,
            departure_date = date_of_departure,
            return_date = date_of_return,
            max_people_count = max_people_count,
            date_created = datetime.now()
        )

        # new_Gig.save() # GIG Object Created!

        RESPONSE["STATUS"] = "Success"
        RESPONSE["GIG_ID"] = new_Gig.id

    else:
        return JsonResponse({"ERROR": "Bad Request"})
        
    
    return JsonResponse(RESPONSE)

def editGigObject(request):
    RESPONSE ={"STATUS": "Failed"}

    if request.method == 'POST':
        if not request.user.profile.is_seller:
            return JsonResponse({"ERROR": "Erm, you need to be a seller, Mr. Hacker :)"})

        # USER IS SELLER

        old_Gig_id = request.POST['original_gig_id']

        # Check if Gig Exists
        if len(Gig.objects.filter(id=old_Gig_id)) == 0:
            return JsonResponse({"ERROR": "Gig Not Found!"})
        
        old_Gig = Gig.objects.get(id=old_Gig_id)


        title = request.POST['title']
        description = request.POST['description']
        price_per_head = request.POST['price_per_head']
        max_people_count = request.POST['max_people_count']
        date_of_expiry_str = request.POST['date_of_expiry_str']
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


        # Return and Terminate if Errors found in Parameter Clutter
        if len(ERRORS) != 0:
            RESPONSE["ERRORS"] = ERRORS
            RESPONSE["ERROR"] = "Submit Request Failed: Inconvinient Data Parameters"
            return JsonResponse(RESPONSE)


        # Edit Gig Object


        
        old_Gig.title = title
        old_Gig.destination = destination
        old_Gig.description = description
        old_Gig.price = price_per_head
        old_Gig.date_of_expiry = date_of_expiry
        old_Gig.departure_date = date_of_departure
        old_Gig.return_date = date_of_return
        old_Gig.max_people_count = max_people_count

        
        

        old_Gig.save() # GIG Object Created!

        RESPONSE["STATUS"] = "Success"
        RESPONSE["GIG_ID"] = old_Gig_id

    else:
        return JsonResponse({"ERROR": "Bad Request"})
        
    
    return JsonResponse(RESPONSE)