from django.contrib import admin
from .models import VideoGame, Stream, Platform

# Register your models here.
admin.site.register(VideoGame)
# register the new Stream Model 
admin.site.register(Stream)
admin.site.register(Platform)