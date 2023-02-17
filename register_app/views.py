from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        e_password = request.POST['e_password']
        c_password = request.POST['c_password']
        if e_password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists in database!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists in database!')
                return redirect('register')
            else:
                user_create = User.objects.create_user(username=username, first_name=first_name,
                                                       last_name=last_name, email=email, password=e_password)
                user_create.save()
                return redirect('register')
        else:
            messages.info(request, 'Please check password entered!')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        e_password = request.POST['e_password']
        user_allowed = auth.authenticate(username=username, password=e_password)
        if user_allowed is not None:
            auth.login(request, user_allowed)
            return redirect('/')
        else:
            messages.info(request, 'Please check password entered!')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
