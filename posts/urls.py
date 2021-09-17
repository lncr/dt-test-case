from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet


router = SimpleRouter()

router.register('posts', PostViewSet)

urlpatterns = []

urlpatterns += router.urls
