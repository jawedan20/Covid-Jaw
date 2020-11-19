from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
from .models import Costumer


# Create your views here.

def index(request):
    """

    """
    context = {
    }
    return render(request, 'base.html', context)
