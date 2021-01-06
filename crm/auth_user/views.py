from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def user_login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        a = login(request, user)
        print(a)
    return render(request, 'auth_user/login.html')
