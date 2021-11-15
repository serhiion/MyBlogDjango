# title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    date_posted = serializers.DateTimeField
    author = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'date_posted', 'author'
        ]
