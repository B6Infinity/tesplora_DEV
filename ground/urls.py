from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.home, name='home'),
    path('home', view=views.home, name='home'),

    # APIs


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)