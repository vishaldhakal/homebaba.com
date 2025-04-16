from rest_framework import serializers
from .models import (
    Country, City, PropertyType, PropertyStatus, 
    Amenity, Tag, Property, PropertyImage, 
    PropertyAmenity, PropertyTag
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'slug', 'flag', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    
    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'country_name', 'slug', 'latitude', 'longitude', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name', 'slug', 'description', 'icon', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class PropertyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyStatus
        fields = ['id', 'name', 'slug', 'color', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'slug', 'icon', 'category', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'property', 'image', 'caption', 'is_primary', 'order', 'created_at']
        read_only_fields = ['created_at']


class PropertyAmenitySerializer(serializers.ModelSerializer):
    amenity_name = serializers.CharField(source='amenity.name', read_only=True)
    
    class Meta:
        model = PropertyAmenity
        fields = ['id', 'property', 'amenity', 'amenity_name', 'created_at']
        read_only_fields = ['created_at']


class PropertyTagSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(source='tag.name', read_only=True)
    
    class Meta:
        model = PropertyTag
        fields = ['id', 'property', 'tag', 'tag_name', 'created_at']
        read_only_fields = ['created_at']


class PropertySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    property_type_name = serializers.CharField(source='property_type.name', read_only=True)
    status_name = serializers.CharField(source='status.name', read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    amenities = PropertyAmenitySerializer(many=True, read_only=True)
    tags = PropertyTagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'slug', 'description', 
            'country', 'country_name', 'city', 'city_name', 
            'address', 'latitude', 'longitude',
            'property_type', 'property_type_name', 'status', 'status_name',
            'price', 'currency', 'bedrooms', 'bathrooms', 'area', 'year_built',
            'is_featured', 'is_active', 'is_verified',
            'images', 'amenities', 'tags',
            'created_at', 'updated_at', 'published_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


# Nested serializers for detailed views
class PropertyDetailSerializer(PropertySerializer):
    country = CountrySerializer(read_only=True)
    city = CitySerializer(read_only=True)
    property_type = PropertyTypeSerializer(read_only=True)
    status = PropertyStatusSerializer(read_only=True) 