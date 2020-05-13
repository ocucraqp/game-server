from rest_framework.routers import DefaultRouter

from server.accounts.views import StatusViewSet

router = DefaultRouter()
router.register(r'status', StatusViewSet, basename='Status')
urlpatterns = router.urls
