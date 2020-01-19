from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Profile,Hood,updates,Businesses,Medicalservices,HealthServices,Adminstration,Post,Comments
from .forms import AccountUpdate,DetailsUpdate, UpdatesForm, ProfileForm,PostForm, BizForm,CommentsForm
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

  
  
  
  return render(request,'profile.html',locals())


@login_required(login_url='/accounts/login/')
def updates(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    current_updates = updates.objects.filter(hood=profile.hood)

    return render(request, 'updates.html', {"updates":current_notifications})

# creting  a profile
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form":form})



@login_required(login_url='/accounts/login/')
def post(request):
    current_user=request.user
    profile = Profile.objects.get(user=current_user)
    posts = Post.objects.filter(hood=profile.hood)

    return render(request, 'post.html', {"posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        form  = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = current_user
            post.hood = profile.hood
            post.save()

        return HttpResponseRedirect('/posts')

    else:
        form =PostForm()

    return render(request, 'post_form.html', {"form":form})





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

@login_required(login_url='/accounts/login/')
def hosy(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    Medicalservices = HealthServices.objects.filter(hood=profile.hood)

    return render(request, 'hosy.html', {"Medicalservice":Medicalservices})
@login_required(login_url='/accounts/login/')

def administration(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    admin=Adminstration.objects.filter(hood=profile.hood)

    return render(request, 'admin.html', locals())
@login_required(login_url='/accounts/login/')
def local_biz(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    biz = Businesses.objects.filter(hood=profile.hood)

    return render(request, 'biz.html', locals())


@login_required(login_url='/accounts/login/')
def new_biz(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == "POST":
        form = BizForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.owner = current_user
            biz.hood = profile.hood
            biz.save()

        return HttpResponseRedirect('/business')

    else:
        form = BizForm()

    return render(request, 'biz_form.html', {"form":form})




@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message = f"{search_term}"


        return render(request, 'search.html', locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})
