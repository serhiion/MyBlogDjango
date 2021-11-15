from django.urls import path

from .api_views import ProfileListAPIView

urlpatterns = [
    path('profiles/', ProfileListAPIView.as_view(), name='post')
]
