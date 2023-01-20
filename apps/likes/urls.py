from rest_framework.routers import DefaultRouter

from apps.likes.views import LikeApiViewSet, CommentLikeApiViewSet


router = DefaultRouter()
router.register(
    prefix="post_like",
    viewset=LikeApiViewSet
)

router.register(
    prefix="comment_like",
    viewset=CommentLikeApiViewSet
)

urlpatterns = router.urls
