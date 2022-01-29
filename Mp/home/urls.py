from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('superUser/',views.superUser,name='superUser'),
    path('login/',views.setLogin,name='login'),
    path('loginOut/',views.loginOut,name='loginOut'),
    path('handlelogin',views.handleLogin,name='handleLogin'),
    path('signup/',views.signup,name='signup'),
    path('handlesignup',views.handleSignup,name='handleSignup'),
    path('adminPage',views.superUser,name='adminpage'),
    path('musicplayer', include('musicplayer.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
