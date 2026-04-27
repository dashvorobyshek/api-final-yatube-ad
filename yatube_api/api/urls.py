from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = router.urls
