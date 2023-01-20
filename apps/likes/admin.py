from django.contrib import admin

from apps.likes.models import Like, CommentLike


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post')

admin.site.register(Like, LikeAdmin)


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'comment')

admin.site.register(CommentLike, CommentLikeAdmin)
