from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #user trying to login
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username is already taken.'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        
        else:
            return render(request, 'accounts/signup.html',{'error':'Passwords need to be match.'})
    else:
        return render(request,'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect.'})

    else:
        return render(request,'accounts/login.html')


def logout(request):
    # this need to be fixed later
    # or maybe now
    if request.method == 'POST': 
        auth.logout(request)
        return redirect('home')

    return render(request,'accounts/signup.html')
