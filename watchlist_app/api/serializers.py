from watchlist_app.models import WatchList, StreamPlatfrom
from django.utils.translation import activate
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

class StreamPlatfromSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatfrom
        fields = '__all__'
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'