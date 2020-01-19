from django.shortcuts import render,redirect
from .models import Profile,Hood,updates,Businesses,Medicalservices,HealthServices,Adminstration,Post,Comments
from .forms import AccountUpdate,DetailsUpdate, UpdatesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
import datetime as datetime

# Create your views here.
def home(request):
    return render(request,'index.html',locals())





@login_required(login_url='/accounts/login/')
def update_profile(request):
  
  if request.method == 'POST':
       user_form = AccountUpdate(request.POST,instance=request.user)
       details_form = DetailsUpdate(request.POST ,request.FILES,instance=request.user.profile)
       if user_form.is_valid() and details_form.is_valid():
          user_form.save()
          details_form.save()
          messages.success(request,f'Your Profile account has been updated successfully')
          return redirect('/')
  else:
  

      user_form = AccountUpdate(instance=request.user)
      
      details_form = DetailsUpdate(instance=request.user.profile) 
  forms = {
    'user_form':user_form,
    'details_form':details_form
  }
  return render(request,'update_profile.html',forms)



@login_required(login_url='/accounts/login/')
def profile(request):
  current_user = request.user
  profile = Profile.objects.filter(user = request.user)

  user_x=User.objects.get(id=request.user.id)
  
  
  return render(request,'profile.html',locals())


@login_required(login_url='/accounts/login/')
def updates(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    updates = updates.objects.filter(hood=profile.hood)

    return render(request, 'updates.html', locals())









@login_required(login_url='/accounts/login/')
def new_update(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    if request.method == "POST":
        form = UpdatesForm(request.POST, request.FILES)
        if form.is_valid():
            updates = form.save(commit=False)
            updates.author = current_user
            updates.hood = profile.hood
            updates.save()

            # if updates.priority == 'High Priority':
            #     send_priority_email(profile.name, profile.email, notification.title, notification.notification, notification.author, notification.neighbourhood)

        return HttpResponseRedirect('/updates')

    else:
        form = UpdatesForm()

    return render(request, 'updates_form.html',locals())

