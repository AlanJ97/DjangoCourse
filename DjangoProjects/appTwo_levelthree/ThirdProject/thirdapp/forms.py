from django import forms
from thirdapp import models
from thirdapp.models import User
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'