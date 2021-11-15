from django.urls import path

from .api_views import ProfileListAPIView

urlpatterns = [
    path('profile/', ProfileListAPIView.as_view(), name='post')
]
