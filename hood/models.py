from django.db import models
from django.db.models import Q
import datetime as dt
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import  post_save





class Hood(models.Model):
     hood_name = models.CharField(max_length = 60)



class Profile(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
  name = models.CharField(max_length=70)
  email = models.EmailField()
  bio = models.CharField(max_length=400)
  picture = models.ImageField(upload_to='profile/')
  hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


  @receiver(post_save,sender=User)
  def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
  @receiver(post_save,sender=User)
  def save_profile(sender, instance,**kwargs):
    instance.profile.save()



class updates(models.Model):
    title = models.CharField(max_length=50)
    notification = models.CharField(max_length=170)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Businesses(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    details = models.CharField(max_length=200)
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    contacts = models.IntegerField()
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Medicalservices(models.Model):
    hospitals = models.CharField(max_length=100)

    def __str__(self):
        return self.hospitals

    def save_hospitals(self):
        self.save()

    @classmethod
    def delete_hospitals(cls, Medicalservices):
        cls.objects.filter(hospitals=hospitals).delete()




class HealthServices(models.Model):
    logo = models.ImageField(upload_to='healthlogo/',default='yumy.jpg')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    Medicalservices = models.ManyToManyField(Medicalservices)

    def __str__(self):
        return self.name


class Adminstration(models.Model):
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=150)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/')
    post = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
       posts = cls.objects.filter(Q (user__user=search_term) | Q (hood__hood=search_term) | Q (title__icontains=search_term))
       return posts


class Comments(models.Model):
    comment = models.CharField(max_length=300,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
 