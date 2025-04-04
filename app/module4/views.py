from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from inventory.models import Category
from .serializers import InventoryCategorySerializer 



# class InventoryCategoryModelViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = InventoryCategorySerializer


# class InventoryCategoryViewSet(ViewSet):
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = InventoryCategorySerializer(queryset, many=True)
#         return Response(serializer.data)


#     @extend_schema(
#         request=InventoryCategorySerializer,
#         responses={201: InventoryCategorySerializer},
#         tags=["Module 4"],
#     )
#     def create(self, request):
#         serializer = InventoryCategorySerializer(data=request.data) 
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



@extend_schema_view(
    list=extend_schema(
        summary="List all inventory categories",
        responses={200: InventoryCategorySerializer(many=True)},
        tags=["Inventory Categories"],
    ),
    create=extend_schema(
        summary="Create a new inventory category",
        request=InventoryCategorySerializer,
        responses={201: InventoryCategorySerializer},
        tags=["Inventory Categories"],
    ),
)
class InventoryCategoryViewSet(ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = InventoryCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = InventoryCategorySerializer(data=request.data) 
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    


