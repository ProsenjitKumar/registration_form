from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username,
                                     first_name=first_name,
                                     last_name=last_name,
                                     email=email,
                                     password=password)
            return HttpResponseRedirect('/registration/')

    else:
        form1 = UserForm()
    return render(request, 'registration.html', {'form': form1})


def loign_user(request):
    return render(request, 'login.html')

