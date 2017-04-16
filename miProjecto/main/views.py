from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    Users = User.objects.all()
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    userExist = checkUser(Users, email, password)
    home = render(request, 'main/home.html', {'message': 'Tus papa'})
    login = render(request, "main/login.html", {'errors': ['Tus muertos']})
    #User.objects.create(email="Bruce", password="Springsteen")
    if userExist:
        return home
    else:
        return login

def register(request):
    name_1 = request.POST.get('name', '')
    email_1 = request.POST.get('email', '')
    username = request.POST.get('username', '')
    password_1 = request.POST.get('password', '')
    confirmPassword = request.POST.get('confirm', '')
    User.objects.create(email=email_1, name=name_1, userName=username, password=password_1)
    return render(request, "main/login.html", {'errors': ['Tus muertos']})

def checkUser(Users, email, password):
    for user in Users:
        if email == user.email and password == user.password:
            return True

def login(request):
    return render(request, "main/login.html")
