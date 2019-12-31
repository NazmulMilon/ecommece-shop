from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    msg = ''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                msg = 'Username Already Taken'
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                msg = 'Email Already Taken'
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                msg = 'User Created Successfully'

    return render(request, 'register.html', {'msg':msg})

