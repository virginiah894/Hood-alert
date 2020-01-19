from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    
    path('', views.home,name='home'),
    path('profile/', views.profile , name = 'profile'),
    path('update_profile/',views.update_profile,name='update'),
    path('updates/', views.updates, name='updates'),
    path('new/update', views.new_update, name = 'newUpdate'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)