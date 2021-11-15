from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import ProfileSerializer
from user.models import Profile


class ProfilePagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'profile_size'
    max_page_size = 10


class ProfileListAPIView(ListAPIView):
    pagination_class = ProfilePagination
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
