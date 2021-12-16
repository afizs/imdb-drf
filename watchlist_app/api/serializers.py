from watchlist_app.models import WatchList, StreamPlatfrom
from django.utils.translation import activate
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatfromSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(read_only=True, many=True)
    # watchlist = serializers.StringRelatedField(many=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie_details'
    )

    class Meta:
        model = StreamPlatfrom
        fields = '__all__'
