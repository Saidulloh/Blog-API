from rest_framework import serializers

from apps.likes.models import Like, CommentLike


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'owner',
            'post',
        )


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = (
            'id',
            'owner',
            'comment',
        )
