from django.urls import path
from . import views

urlpatterns = [
    # Country endpoints
    path('countries/', views.CountryListCreateView.as_view(), name='country-list'),
    path('countries/<slug:slug>/', views.CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    
    # City endpoints
    path('cities/', views.CityListCreateView.as_view(), name='city-list'),
    path('cities/<slug:slug>/', views.CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
    
    # PropertyType endpoints
    path('property-types/', views.PropertyTypeListCreateView.as_view(), name='property-type-list'),
    path('property-types/<slug:slug>/', views.PropertyTypeRetrieveUpdateDestroyView.as_view(), name='property-type-detail'),
    
    # PropertyStatus endpoints
    path('property-statuses/', views.PropertyStatusListCreateView.as_view(), name='property-status-list'),
    path('property-statuses/<slug:slug>/', views.PropertyStatusRetrieveUpdateDestroyView.as_view(), name='property-status-detail'),
    
    # Amenity endpoints
    path('amenities/', views.AmenityListCreateView.as_view(), name='amenity-list'),
    path('amenities/<slug:slug>/', views.AmenityRetrieveUpdateDestroyView.as_view(), name='amenity-detail'),
    
    # Tag endpoints
    path('tags/', views.TagListCreateView.as_view(), name='tag-list'),
    path('tags/<slug:slug>/', views.TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
    
    # Property endpoints
    path('properties/', views.PropertyListCreateView.as_view(), name='property-list'),
    path('properties/<slug:slug>/', views.PropertyRetrieveUpdateDestroyView.as_view(), name='property-detail'),
    
    # PropertyImage endpoints
    path('property-images/', views.PropertyImageListCreateView.as_view(), name='property-image-list'),
    path('property-images/<int:pk>/', views.PropertyImageRetrieveUpdateDestroyView.as_view(), name='property-image-detail'),
    
    # PropertyAmenity endpoints
    path('property-amenities/', views.PropertyAmenityListCreateView.as_view(), name='property-amenity-list'),
    path('property-amenities/<int:pk>/', views.PropertyAmenityRetrieveUpdateDestroyView.as_view(), name='property-amenity-detail'),
    
    # PropertyTag endpoints
    path('property-tags/', views.PropertyTagListCreateView.as_view(), name='property-tag-list'),
    path('property-tags/<int:pk>/', views.PropertyTagRetrieveUpdateDestroyView.as_view(), name='property-tag-detail'),
] 