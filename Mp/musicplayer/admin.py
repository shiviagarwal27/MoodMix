from django.contrib import admin


# Register your models here.
from .models import MusicDB, Contact

admin.site.register(MusicDB)
admin.site.register(Contact)