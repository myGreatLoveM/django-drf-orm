from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from inventory.models import Category, Product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import (
    CategorySerializer,
    CreateProductSerializer,
    CreateProductStockSerializer,
    ProductSerializer,
    ProductStockSerializer,
)

# class InventoryCategoryModelViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryViewSet(ViewSet):
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)


#     @extend_schema(
#         request=CategorySerializer,
#         responses={201: CategorySerializer},
#         tags=["Module 4"],
#     )
#     def create(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        responses={200: CategorySerializer(many=True)},
        tags=["Categories"],
    ),
    create=extend_schema(
        summary="Create a new category",
        request=CategorySerializer,
        responses={201: CategorySerializer},
        tags=["Categories"],
    ),
    retrieve=extend_schema(
        summary="Get category with pk",
        parameters=[OpenApiParameter("id", type=int, location=OpenApiParameter.PATH)],
        responses={200: CategorySerializer},
        tags=["Categories"],
    ),
    update=extend_schema(
        summary="Update existing category",
        request=CategorySerializer,
        parameters=[OpenApiParameter("id", type=int, location=OpenApiParameter.PATH)],
        responses={200: CategorySerializer},
        tags=["Categories"],
    ),
    partial_update=extend_schema(
        summary="Partial Update existing category",
        request=CategorySerializer,
        parameters=[OpenApiParameter("id", type=int, location=OpenApiParameter.PATH)],
        responses={200: CategorySerializer},
        tags=["Categories"],
    ),
)
class CategoryViewSet(ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {"error": f"Category with id {pk} not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist:
            return Response(
                {"error": f"Category with id {pk} not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def partial_update(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Category.DoesNotExist:
            return Response(
                {"error": f"Category with id {pk} not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )


@extend_schema_view(
    create=extend_schema(
        summary="Create a bulk of categories",
        request=CategorySerializer(many=True),
        responses={201: CategorySerializer(many=True)},
        tags=["Categories"],
    ),
)
class CategoryBulkCreateViewSet(ViewSet):
    def create(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        categories = [Category(**cat_item) for cat_item in serializer.validated_data]
        category_objs = Category.objects.bulk_create(categories)
        resp_data = CategorySerializer(category_objs, many=True).data
        return Response(resp_data, status=status.HTTP_201_CREATED)


@extend_schema_view(
    list=extend_schema(
        summary="List all product",
        responses={200: ProductSerializer(many=True)},
        tags=["Products"],
    ),
    create=extend_schema(
        summary="Create a product",
        request=CreateProductSerializer,
        responses={201: ProductSerializer},
        tags=["Products"],
    ),
)
class ProductViewSet(ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema_view(
    list=extend_schema(
        summary="List all product",
        responses={200: ProductStockSerializer(many=True)},
        tags=["Products-stocks"],
    ),
    create=extend_schema(
        summary="Create a product with stock data",
        request=CreateProductStockSerializer,
        responses={201: CreateProductStockSerializer},
        tags=["Products-stocks"],
    ),
)
class ProductStockViewSet(ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductStockSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateProductStockSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
