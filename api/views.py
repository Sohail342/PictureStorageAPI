from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Picture, Category
from .serializers import (
    PictureSerializer,
    CategorySerializer,
CategoryPicturesSerializer,
)

class Pictures(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class CategoryPictures(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoryPicturesSerializer

    def get_queryset(self):
        category_id = self.kwargs['pk']
        from icecream import ic
        category = Category.objects.filter(id=category_id)
        return category

class Categories(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer