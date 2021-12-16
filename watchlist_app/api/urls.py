
from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformList, StreamPlatformDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list' ),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformList.as_view(), name='stream_list' ),
    path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='stream_detail' ),

]
