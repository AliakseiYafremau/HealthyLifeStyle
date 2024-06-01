import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics, permissions
from .serializers import *
from .models import *


# Дженерики создания
class CategoryViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = 'name'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class DishHalfViewSet(generics.ListCreateAPIView):
    queryset = DishHalf.objects.all()
    serializer_class = DishHalfSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'category', 'calories',
                        'proteins', 'fats', 'carbs',
                        'price', 'contraindications', 'rating']
    search_fields = ['name', 'category', 'calories',
                        'proteins', 'fats', 'carbs',
                        'price', 'contraindications', 'rating']
    ordering_fields = ['name', 'category', 'calories',
                        'proteins', 'fats', 'carbs',
                        'price', 'contraindications', 'rating']
    ordering = '-rating'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class CombinationViewSet(generics.ListCreateAPIView):
    queryset = Combination.objects.all()
    serializer_class = CombinationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['half1', 'half2']
    search_fields = ['half1', 'half2']
    ordering_fields = ['half1', 'half2']

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class AllergyViewSet(generics.ListCreateAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = 'name'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class ArticleViewSet(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'date_created', 'text']
    search_fields = ['author', 'date_created', 'text']
    ordering_fields = ['author', 'date_created', 'text']
    ordering = '-date_created'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']
