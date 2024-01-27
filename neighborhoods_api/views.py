# views.py

from rest_framework import generics
from .models import Blog1, Blog2, Blog1Category, Blog2Category, BoardMinutes
from .serializers import Blog1Serializer, Blog2Serializer, Blog1CategorySerializer, Blog2CategorySerializer, BoardMinutesSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group


# listing all blog1s for a neighborhood
class Blog1ListByNeighborhood(generics.ListAPIView):
    serializer_class = Blog1Serializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        return Blog1.objects.filter(neighborhood__name=neighborhood_name)
    
# listing all blog1 categoriess for a neighborhood
class Blog1CategoryListByNeighborhood(generics.ListAPIView):
    serializer_class = Blog1CategorySerializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        return Blog1Category.objects.filter(neighborhood__name=neighborhood_name)

# listing all blog2s for a neighborhood
class Blog2ListByNeighborhood(generics.ListAPIView):
    serializer_class = Blog2Serializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        return Blog2.objects.filter(neighborhood__name=neighborhood_name)
    

# listing all blog2 categories for a neighborhood
class Blog2CategoryListByNeighborhood(generics.ListAPIView):
    serializer_class = Blog2CategorySerializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        return Blog2Category.objects.filter(neighborhood__name=neighborhood_name)

# listing all board minutes for a neighborhood
class BoardMinutesListByNeighborhood(generics.ListAPIView):
    serializer_class = BoardMinutesSerializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        return BoardMinutes.objects.filter(neighborhood__name=neighborhood_name)

# listing all blog1s by category and neighborhood
class Blog1ListByCategoryAndNeighborhood(generics.ListAPIView):
    serializer_class = Blog1Serializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        category_name = self.kwargs['category_name']

        # Get the neighborhood and category objects
        neighborhood = get_object_or_404(Group, name=neighborhood_name)
        category = get_object_or_404(Blog1Category, neighborhood=neighborhood, name=category_name)

        # Filter Blog1 instances by neighborhood and category
        queryset = Blog1.objects.filter(neighborhood=neighborhood, categories=category)

        return queryset
    

# listing all blog2s by category and neighborhood
class Blog2ListByCategoryAndNeighborhood(generics.ListAPIView):
    serializer_class = Blog2Serializer

    def get_queryset(self):
        neighborhood_name = self.kwargs['neighborhood_name']
        category_name = self.kwargs['category_name']

        # Get the neighborhood and category objects
        neighborhood = get_object_or_404(Group, name=neighborhood_name)
        category = get_object_or_404(Blog2Category, neighborhood=neighborhood, name=category_name)

        # Filter Blog1 instances by neighborhood and category
        queryset = Blog2.objects.filter(neighborhood=neighborhood, categories=category)

        return queryset