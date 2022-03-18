from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect, request

from .models import Adminstration

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Numero'}))


class Enseingantloginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Nom de l'utilisateur"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mot de passe'}))


