from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('/addsong', views.addSong,name='addSong'),
    path('/search', views.search,name='search'),
    path('/controlsearch', views.controlSearch,name='controlSearch'),
    path('/control', views.control,name='control'),
    path('/edit/<int:song_id>', views.edit,name='edit'),
    path('/delete/<int:song_id>', views.delete,name='delete'),
    path('/contact', views.contact,name='contact'),
    path('/contactInfo', views.contactInfo,name='contactInfo'),
    path('/about', views.about,name='about'),
    path('/viewall/<str:song_category>', views.viewAll,name='viewAll'),
]
