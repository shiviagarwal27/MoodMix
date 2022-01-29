import os
from math import ceil

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.messages import constants as message
# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from musicplayer.models import MusicDB


def home(request):
    allSongs = []
    catprods = MusicDB.objects.values('song_category', 'song_id')
    cats = {item['song_category'] for item in catprods}
    for cat in cats:
        songs = MusicDB.objects.filter(song_category=cat)
        n = len(songs)
        nSlide = (n // 4) + ceil((n / 4) - (n // 4))
        allSongs.append([songs, range(1, nSlide), nSlide])
    params = {"allSongs": allSongs}
    return render(request, 'home/index.html', params)


@csrf_exempt
def setLogin(request):
    return redirect('handleLogin')


@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['uname']
        loginpassword = request.POST['pass']
        user = authenticate(username=loginusername, password=loginpassword)
        superusers = User.objects.filter(is_superuser=True)
        print(superusers)
        print(user)
        if user in superusers:
            login(request, user)
            return redirect('superUser')
        if user is not None:
            login(request, user)
            # message.success(request,"Sussessfully Log in")
            return redirect('/musicplayer')
        else:
            # message.error(request,"Invalid Criteria Please try again")
            return redirect('login')
    return render(request, 'home/login.html', {'context': RequestContext(request)})


@csrf_exempt
def signup(request):
    return redirect('handleSignup')


@csrf_exempt
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) < 5:
            return HttpResponse("<h2>username error<h2><br><li><a href='/login'>Log in</a></li><br><li><a  "
                                "href='/signup'>Sign Up</a></li>")
        if User.objects.filter(username=username).exists():
            return HttpResponse("<h2>Username already exist<h2><br><li><a href='/login'>Log in</a></li><br><li><a  "
                                "href='/signup'>Sign Up</a></li>")
        if pass1 != pass2:
            # message.error(request,"Password Not Matched")
            return HttpResponse("<h2>pass error<h2><br><li><a href='/login'>Log in</a></li><br><li><a  "
                                "href='/signup'>Sign Up</a></li>")
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        login(request, myuser)
        # message.success(request,"Your Account has been Created Succeessfully")
        return redirect('/musicplayer')
    return render(request, 'home/signup.html')


def loginOut(request):
    logout(request)
    return redirect('/')


def superUser(request):
    return render(request, 'musicplayer/admin.html')
