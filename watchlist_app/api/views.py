from watchlist_app.models import WatchList, StreamPlatfrom
from rest_framework import status
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatfromSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class StreamPlatformList(APIView):
    def get(self, request):
        streams = StreamPlatfrom.objects.all()
        serializer = StreamPlatfromSerializer(streams, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatfromSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class StreamPlatformDetail(APIView):
    def get(self, request, pk):
        try:
            movie = StreamPlatfrom.objects.get(pk=pk)
        except StreamPlatfrom.DoesNotExist:
            return Response({'Error': 'Movie does not exits'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatfromSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = StreamPlatfrom.objects.get(pk=pk)
        serializer = StreamPlatfromSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        movie = StreamPlatfrom.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class WatchListDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie does not exits'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)