from . import views
from inspect import getmembers, isclass
from rest_framework.viewsets import ViewSet
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryBulkCreateViewSet, ProductViewSet


router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename='categories')
router.register(r"categories-bulk", CategoryBulkCreateViewSet, basename="categories-bulk")
router.register(r"products", ProductViewSet, basename="products")


urlpatterns = router.urls


for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        print(name, cls)




