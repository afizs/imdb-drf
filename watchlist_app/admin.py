from django.contrib import admin

# Register your models here.
from watchlist_app.models import WatchList, StreamPlatfrom

admin.site.register(WatchList)
admin.site.register(StreamPlatfrom)
