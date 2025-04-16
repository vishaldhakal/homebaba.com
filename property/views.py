from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import (
    Country, City, PropertyType, PropertyStatus, 
    Amenity, Tag, Property, PropertyImage, 
    PropertyAmenity, PropertyTag
)
from .serializers import (
    CountrySerializer, CitySerializer, PropertyTypeSerializer, PropertyStatusSerializer,
    AmenitySerializer, TagSerializer, PropertySerializer, PropertyImageSerializer,
    PropertyAmenitySerializer, PropertyTagSerializer, PropertyDetailSerializer
)


# Country views
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'code']


class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# City views
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'country__name']
    filterset_fields = ['country']


class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# PropertyType views
class PropertyTypeListCreateView(generics.ListCreateAPIView):
    queryset = PropertyType.objects.filter(is_active=True)
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PropertyTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# PropertyStatus views
class PropertyStatusListCreateView(generics.ListCreateAPIView):
    queryset = PropertyStatus.objects.filter(is_active=True)
    serializer_class = PropertyStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class PropertyStatusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyStatus.objects.all()
    serializer_class = PropertyStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# Amenity views
class AmenityListCreateView(generics.ListCreateAPIView):
    queryset = Amenity.objects.filter(is_active=True)
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'category']
    filterset_fields = ['category']


class AmenityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# Tag views
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# Property views
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description', 'address', 'country__name', 'city__name']
    filterset_fields = ['country', 'city', 'property_type', 'status', 'is_featured', 'is_verified']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
            
        # Filter by bedrooms
        bedrooms = self.request.query_params.get('bedrooms', None)
        if bedrooms is not None:
            queryset = queryset.filter(bedrooms__gte=bedrooms)
            
        # Filter by bathrooms
        bathrooms = self.request.query_params.get('bathrooms', None)
        if bathrooms is not None:
            queryset = queryset.filter(bathrooms__gte=bathrooms)
            
        # Filter by area
        min_area = self.request.query_params.get('min_area', None)
        max_area = self.request.query_params.get('max_area', None)
        
        if min_area is not None:
            queryset = queryset.filter(area__gte=min_area)
        if max_area is not None:
            queryset = queryset.filter(area__lte=max_area)
            
        # Filter by amenities
        amenities = self.request.query_params.get('amenities', None)
        if amenities is not None:
            amenity_ids = amenities.split(',')
            for amenity_id in amenity_ids:
                queryset = queryset.filter(amenities__id=amenity_id)
                
        # Filter by tags
        tags = self.request.query_params.get('tags', None)
        if tags is not None:
            tag_ids = tags.split(',')
            for tag_id in tag_ids:
                queryset = queryset.filter(tags__id=tag_id)
                
        return queryset


class PropertyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


# PropertyImage views
class PropertyImageListCreateView(generics.ListCreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property', 'is_primary']


class PropertyImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# PropertyAmenity views
class PropertyAmenityListCreateView(generics.ListCreateAPIView):
    queryset = PropertyAmenity.objects.all()
    serializer_class = PropertyAmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property', 'amenity']


class PropertyAmenityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyAmenity.objects.all()
    serializer_class = PropertyAmenitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# PropertyTag views
class PropertyTagListCreateView(generics.ListCreateAPIView):
    queryset = PropertyTag.objects.all()
    serializer_class = PropertyTagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property', 'tag']


class PropertyTagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyTag.objects.all()
    serializer_class = PropertyTagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
