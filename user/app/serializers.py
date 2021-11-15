from rest_framework import serializers

from user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=True)
    image = serializers.ImageField

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'image'
        ]
