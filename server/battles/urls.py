from rest_framework.routers import DefaultRouter
from server.battles.views import BattlesViewSet

router = DefaultRouter()
router.register(r'battles', BattlesViewSet, basename='battles')
urlpatterns = router.urls