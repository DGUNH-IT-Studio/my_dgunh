from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 



def index(request):
    data = {
        }
    return render(request, 'auth/index.html')

def signup(request):
    data = {
        }
    
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['fname']
        surname = request.POST['sname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        new_user = User.objects.create(username, email, password1)
        new_user.first_name = first_name
        new_user.surname = surname
        new_user.last_name = last_name

        new_user.save()

        messages.success(request, "Your account have been successfully created.")

        return redirect('')

    return render(request, 'auth/signup.html')

def login(request):
    data = {
        }
    return render(request, 'auth/login.html')

def logout(request):
    data = {
        }
    return render(request, 'auth/logout.html')
