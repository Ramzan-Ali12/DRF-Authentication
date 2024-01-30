from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema


# add products
@extend_schema(request=ProductSerializer)
@api_view(["POST"])
def add(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Success": "Product addedd Successfullu",
                    "newProduct": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": "invalid request"},
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


@extend_schema(request=ProductSerializer)
@api_view(["PUT"])
def edit(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"error": "product not found!!"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": "product updated Successfully",
                "updatedProduct": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# getAll products
@extend_schema(request=ProductSerializer)
@api_view(["GET"])
def getAll(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(
            {"success": "Products found successfully", "products": serializer.data},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


# delete products
@extend_schema(request=ProductSerializer)
@api_view(["DELETE"])
def delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found or deleted!!"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "DELETE":
        product.delete()
        return Response(
            {"success": "Product deleted successfully!!"},
            status=status.HTTP_200_OK,
        )

    return Response({"error": "invalid request!"}, status=status.HTTP_400_BAD_REQUEST)
