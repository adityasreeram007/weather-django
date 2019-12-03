from django import forms
#from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
#from weathere.models import logg
from django.forms import ModelForm
from weathere.models import logg,regg
class authform(forms.ModelForm):
    #print(1)
    class Meta:
        model=logg
        fields=['user','passer']
class regform(forms.ModelForm):
    class Meta:
        model=regg
        fields=['user','passer','confpasser','email']
    
    
        