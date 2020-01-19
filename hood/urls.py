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
    path('posts', views.post, name='post'),
    path('new/post', views.new_post, name='newPost'),
    path('health', views.hosy, name='hosy'),
    path('search', views.search_results, name = 'search_results'),

    path('adminst', views.administration, name='admin'),
    path('business', views.local_biz, name='biz'),
    path('new/business', views.new_biz, name='newBiz'),


    path('create/profile',views.create_profile, name='createProfile'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)