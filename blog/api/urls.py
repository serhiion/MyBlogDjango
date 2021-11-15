from django.urls import path

from .api_views import PostListAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post')
]