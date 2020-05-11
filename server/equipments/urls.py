from rest_framework.routers import DefaultRouter

from server.equipments.views import WeaponViewSet

router = DefaultRouter()
router.register(r'weapons', WeaponViewSet, basename='weapons')
urlpatterns = router.urls
