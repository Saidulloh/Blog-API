from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post
from apps.comments.models import Comment


User = get_user_model()


class Like(models.Model):
    """
    Model for likes
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='like_owner',
        verbose_name='like_owner'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post',
        verbose_name='post'
    )

    def __str__(self):
        return f'{self.id} -- {self.post.title}'

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'Likes'


class CommentLike(models.Model):
    """
    Model for comment likes
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='comment_like_owner',
        verbose_name='comment_like_owner'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment',
        verbose_name='comment'
    )

    def __str__(self):
        return f'{self.id} -- {self.comment.title}'

    class Meta:
        verbose_name = 'comment like'
        verbose_name_plural = 'Comment likes'
