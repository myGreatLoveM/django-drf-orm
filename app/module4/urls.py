from inspect import getmembers, isclass

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

from . import views
from .views import (
    CategoryBulkCreateViewSet,
    CategoryViewSet,
    ProductStockViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(
    r"categories-bulk", CategoryBulkCreateViewSet, basename="categories-bulk"
)
router.register(r"products", ProductViewSet, basename="products")
router.register(r"products-stocks", ProductStockViewSet, basename="products-stocks")


urlpatterns = router.urls


for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        print(name, cls)

