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

    # APIs

    path('check_if_username_exists', view=views.checkifusernameexists, name='checkifusernameexists'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)