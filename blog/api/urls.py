from django.urls import path

from .api_views import PostListAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post')
]