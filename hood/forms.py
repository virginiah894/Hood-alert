from .models import Profile,Hood
from .models import Profile,Hood,updates,Businesses,Medicalservices,HealthServices,Adminstration,Post,Comments

from django.contrib.auth.models import User
from django  import forms
from crispy_forms.helper import FormHelper
from  crispy_forms.layout import Submit,Layout,Field






class AccountUpdate(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']


class DetailsUpdate(forms.ModelForm):
  class Meta:
    model = Profile
    exclude= ['user']  




class UpdatesForm(forms.ModelForm):
    class Meta:
        model = updates
        exclude = ['editor', 'hood', 'created_date']
