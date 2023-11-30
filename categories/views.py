from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from django.http import Http404

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            category=Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)

