from rest_framework.routers import DefaultRouter
from ..views import AssignmentViewSet


router = DefaultRouter()
router.register(r'', AssignmentViewSet, base_name='assignments')
urlpatterns = router.urls