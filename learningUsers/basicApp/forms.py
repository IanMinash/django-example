from django import forms
from django.contrib.auth.models import User
from basicApp import models

class userForm(forms.ModelForm):
    """Form definition for user."""
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        """Meta definition for userform."""

        model = User
        fields = ('username','email','password')


class userProfileForm(forms.ModelForm):
    """Form definition for userProfile."""
    
    class Meta:
        """Meta definition for userProfileform."""

        model = models.userProfile
        fields = ('portfolio_site', 'profile_pic')
