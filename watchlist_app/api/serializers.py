from watchlist_app.models import Movie
from django.utils.translation import activate
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

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