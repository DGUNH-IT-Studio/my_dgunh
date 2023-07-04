from django.shortcuts import render

def index(request):
    data = {
        }
    return render(request, 'auth/index.html')

def signup(request):
    data = {
        }
    return render(request, 'auth/signup.html')

def login(request):
    data = {
        }
    return render(request, 'auth/login.html')

def logout(request):
    data = {
        }
    return render(request, 'auth/logout.html')
