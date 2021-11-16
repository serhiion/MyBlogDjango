from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, PostCreateSerializer
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


class CreatePostAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['author'] = request.user
        serializer.create(serializer.validated_data)
        return Response(serializer.data)


class DetailPostAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePostAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class GetByTitle(APIView):
    # def get_object(self, title):
    #     try:
    #         return Post.objects.get(title=title)
    #     except Post.DoesNotExist:
    #         raise Http404

    def get(self, request, **kwargs):
        print(kwargs)
        # return Response(200)
        queryset = Post.objects.filter(title=kwargs['title'])
        post_list = [PostSerializer(i).data for i in queryset]
        print(post_list)
        # serializer = PostSerializer(queryset)
        # print(serializer.data)
        # object = self.get_object(kwargs['title'])
        # serializer = PostSerializer(object)
        return Response(data=post_list, status=200)
