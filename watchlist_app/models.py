from django.db import models

class StreamPlatfrom(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    platfrom = models.ForeignKey(StreamPlatfrom, on_delete=models.CASCADE, related_name='watchlist')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title