from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.home, name='home'),
    path('home', view=views.home, name='home'),
    path('loginorsignup', view=views.loginorsignup, name='loginorsignup'),
    path('login', view=views.loginorsignup, name='loginorsignup'),
    path('signup', view=views.loginorsignup, name='loginorsignup'),
    path('profile-<str:username>', view=views.view_profile, name='view_profile'),
    path('creategig', view=views.creategig, name='creategig'),
    path('viewgig-<str:gig_id>', view=views.viewgig, name='viewgig'),

    # APIs

    path('check_if_username_exists', view=views.checkifusernameexists, name='checkifusernameexists'),
    path('submit_gig', view=views.createGigObject, name='submit_gig'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)