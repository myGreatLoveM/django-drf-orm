from . import views
from inspect import getmembers, isclass
from rest_framework.viewsets import ViewSet
from rest_framework.routers import DefaultRouter
from .views import InventoryCategoryViewSet


router = DefaultRouter()
router.register(r"inventory-category", InventoryCategoryViewSet, basename='inventory-category')


urlpatterns = router.urls


for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        print(name, cls)