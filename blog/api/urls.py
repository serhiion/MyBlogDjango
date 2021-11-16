from django.urls import path

from .api_views import PostListAPIView, CreatePostAPIView, DetailPostAPIView, \
    DeletePostAPIView, UpdatePostAPIView, GetByTitle

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post'),
    path('create/', CreatePostAPIView.as_view(), name='create_post'),
    path('detail/<int:pk>', DetailPostAPIView.as_view(), name='detail'),
    path('delet/<int:pk>', DeletePostAPIView.as_view(), name='delet'),
    path('update/<int:pk>', UpdatePostAPIView.as_view(), name='update'),
    path('get_by_title/<str:title>', GetByTitle.as_view(), name='get_by_title'),
]