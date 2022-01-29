from math import ceil

import wordninja
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MusicDB, Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    allSongs = []
    catprods = MusicDB.objects.values('song_category', 'song_id')
    cats = {item['song_category'] for item in catprods}
    for cat in cats:
        songs = MusicDB.objects.filter(song_category=cat)
        n = len(songs)
        nSlide = (n // 4) + ceil((n / 4) - (n // 4))
        allSongs.append([songs, range(1, nSlide), nSlide])
    params = {"allSongs": allSongs}
    print(params)
    return render(request, 'musicplayer/index.html', params)


def addSong(request):
    if request.method == 'POST':
        sng = request.FILES['songa']
        img = request.FILES['imagea']
        sname = request.POST['song_name']
        artist = request.POST['artist']
        mname = request.POST['movie_name']
        category = request.POST['category']
        emo = request.POST['emotions']
        emoji = request.POST['emojies']
        addMusic = MusicDB(song_name=sname, song_artist=artist, movie_name=mname, song_category=category, emotions=emo,
                           emojies=emoji,
                           song=sng, image=img)
        addMusic.save()
    return render(request, 'musicplayer/admin.html')


def control(request):
    music = MusicDB.objects.all()
    params = {"music": music}
    return render(request, 'musicplayer/control.html', params)


def edit(request, song_id):
    try:
        if request.method == "POST":
            sid = request.POST['id']
            sag = str(sid)
            sng = request.FILES['son']
            img = request.FILES['ima']
            sname = request.POST['song_name']
            artist = request.POST['artist']
            mname = request.POST['movie_name']
            category = request.POST['category']
            emoji = request.POST['emo']
            emo = request.POST['emotions']
            if song_id != '0':
                music = MusicDB.objects.get(song_id=song_id)
                music.song_id = sid
                music.song_name = sname
                music.song_artist = artist
                music.movie_name = mname
                music.song_category = category
                music.emojies = emoji
                music.emotions = emo
                music.song = sng
                music.image = img
                music.save()
                return redirect('/musicplayer/edit/' + sag)
    except:
        try:
            if request.method == "POST":
                sid = request.POST['id']
                sag = str(sid)
                sng = request.FILES['son']
                sname = request.POST['song_name']
                artist = request.POST['artist']
                mname = request.POST['movie_name']
                category = request.POST['category']
                emoji = request.POST['emo']
                emo = request.POST['emotions']
                if song_id != '0':
                    music = MusicDB.objects.get(song_id=song_id)
                    music.song_id = sid
                    music.song_name = sname
                    music.song_artist = artist
                    music.movie_name = mname
                    music.song_category = category
                    music.emojies = emoji
                    music.emotions = emo
                    music.song = sng
                    music.save()
                    return redirect('/musicplayer/edit/' + sag)
        except:
            try:
                if request.method == "POST":
                    sid = request.POST['id']
                    sag = str(sid)
                    img = request.FILES['ima']
                    sname = request.POST['song_name']
                    artist = request.POST['artist']
                    mname = request.POST['movie_name']
                    category = request.POST['category']
                    emoji = request.POST['emo']
                    emo = request.POST['emotions']
                    if song_id != '0':
                        music = MusicDB.objects.get(song_id=song_id)
                        music.song_id = sid
                        music.song_name = sname
                        music.song_artist = artist
                        music.movie_name = mname
                        music.song_category = category
                        music.emojies = emoji
                        music.emotions = emo
                        music.image = img
                        music.save()
                        return redirect('/musicplayer/edit/' + sag)
            except:
                if request.method == "POST":
                    sid = request.POST['id']
                    sag = str(sid)
                    sname = request.POST['song_name']
                    artist = request.POST['artist']
                    mname = request.POST['movie_name']
                    category = request.POST['category']
                    emoji = request.POST['emo']
                    emo = request.POST['emotions']
                    if song_id != '0':
                        music = MusicDB.objects.get(song_id=song_id)
                        music.song_id = sid
                        music.song_name = sname
                        music.song_artist = artist
                        music.movie_name = mname
                        music.song_category = category
                        music.emotions = emo
                        music.emojies = emoji
                        music.save()
                        return redirect('/musicplayer/edit/' + sag)
    music = MusicDB.objects.filter(song_id=song_id)
    return render(request, 'musicplayer/edit.html', {'music': music[0]})


def delete(request, song_id):
    MusicDB.objects.filter(song_id=song_id).delete()
    return redirect('control')


def viewAll(request, song_category):
    allSongs = []
    music = MusicDB.objects.filter(song_category=song_category)
    n = len(music)
    allSongs.append([music, range(1, n)])
    params = {"allSongs": allSongs, "song_category": song_category}
    return render(request, 'musicplayer/viewall.html', params, )


def contact(request):
    if request.method == 'POST':
        first = request.POST['fname']
        last = request.POST['lname']
        emai = request.POST['email']
        phon = request.POST['pno']
        texte = request.POST['text']
        if len(first) < 2 or len(emai) < 3 or len(phon) < 10 or len(texte) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contacts = Contact(first_name=first, last_name=last, email=emai, phone=phon, desc=texte)
            contacts.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'musicplayer/contact.html')


def contactInfo(request):
    cont = Contact.objects.all()
    params = {"cont": cont}
    return render(request, 'musicplayer/contactInfo.html', params)


def about(request):
    return render(request, 'musicplayer/about.html')


def match(query, item):
    print("running")
    # print(item)
    b = wordninja.split(query.lower())
    a = wordninja.split(item)
    n = range(0, len(a))
    m = range(0, len(b))
    try:
        for i in m:
            for j in n:
                print(b[i], a[j])
                if b[i] == a[j]:
                    print(b[i],a[j])
                    return True
                else:
                    continue
    except:
        return False


# impliment testme named file logic

def searchMatch(query, item):
    if (query.lower() in item.song_name.lower() or
            query.lower() in item.song_artist.lower() or
            query.lower() in item.movie_name.lower() or
            query.lower() in item.song_category.lower() or
            query.lower() in item.emotions.lower() or
            query in item.emojies
    ):
        print('1')
        return True
    elif (item.song_name.lower() in query.lower() or
          item.song_artist.lower() in query.lower() or
          item.movie_name.lower() in query.lower() or
          item.song_category.lower() in query.lower() or
          item.emotions.lower() in query.lower()
    ):
        print('2')
        return True
    elif match(query, item.emotions.lower()):
        print('r')
        return True
    elif match(query, item.song_category.lower()):
        print('r')
        return True
    else:
        return False


def search(request):
    query = request.GET['search']
    allSongs = []
    catsongs = MusicDB.objects.values('song_category', 'song_id')
    cats = {item['song_category'] for item in catsongs}
    for cat in cats:
        songtemp = MusicDB.objects.filter(song_category=cat)
        music = [item for item in songtemp if searchMatch(query, item)]
        if len(query) < 3:
            return redirect('home')
        if len(music) != 0:
            n = len(music)
            allSongs.append([music, range(1, n)])
    params = {'allSongs': allSongs, 'query': query}
    return render(request, 'musicplayer/search.html', params)


def controlSearchMatch(query, item):
    if (query.lower() in item.song_name.lower() or
            query.lower() in item.song_artist.lower() or
            query.lower() in item.movie_name.lower() or
            query.lower() in item.song_category.lower() or
            query.lower() in item.emotions.lower() or
            query in item.emojies):
        return True
    else:
        return False


def controlSearch(request):
    query = request.GET['search']
    allSongs = []
    catsongs = MusicDB.objects.values('song_category', 'song_id')
    cats = {item['song_category'] for item in catsongs}
    for cat in cats:
        songtemp = MusicDB.objects.filter(song_category=cat)
        music = [item for item in songtemp if controlSearchMatch(query, item)]
        if len(query) < 3:
            return redirect('control')
        if len(music) != 0:
            n = len(music)
            allSongs.append([music, range(1, n)])
    params = {'allSongs': allSongs, 'query': query}
    return render(request, 'musicplayer/controlsearch.html', params)
