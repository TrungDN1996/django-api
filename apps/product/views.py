from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer

@extend_schema(tags=["Products"])
class ProductViewSet(ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(
            {"detail": "Product successfully deleted."},
            status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['patch'], url_path='activate-product')
    def activate(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        activate = request.data.get('activate')
        if activate is not None:
            product.activate = activate
            product.save()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
