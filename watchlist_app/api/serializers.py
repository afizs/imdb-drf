from watchlist_app.models import Movie
from django.utils.translation import activate
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
    
    def get_len_name(self, object):
        return len(object.name)


    def validate_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Description is too short')
        else:
            return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description both are same.')
        else:
            return data