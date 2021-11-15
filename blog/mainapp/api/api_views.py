from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from blog.models import Post
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class PostListAPIView(ListAPIView):
    pagination_class = PostPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()
