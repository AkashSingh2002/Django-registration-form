from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return HttpResponse("hi {name} You Logged in Sucessfully!",{name:username})
        else:
            messages.error(request, "Please Register first")
            return redirect('register')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, fname, lname, phone, email, password)
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('home')
    return render(request, 'register.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
