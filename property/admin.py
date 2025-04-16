from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    Country, City, PropertyType, PropertyStatus, 
    Amenity, Tag, Property, PropertyImage, 
    PropertyAmenity, PropertyTag
)

@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'code')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ('name', 'country', 'is_active', 'created_at')
    list_filter = ('is_active', 'country')
    search_fields = ('name', 'country__name')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


@admin.register(PropertyType)
class PropertyTypeAdmin(ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


@admin.register(PropertyStatus)
class PropertyStatusAdmin(ModelAdmin):
    list_display = ('name', 'color', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


@admin.register(Amenity)
class AmenityAdmin(ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'created_at')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    fields = ('image', 'caption', 'is_primary', 'order')


class PropertyAmenityInline(admin.TabularInline):
    model = PropertyAmenity
    extra = 1


class PropertyTagInline(admin.TabularInline):
    model = PropertyTag
    extra = 1


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ('title', 'country', 'city', 'property_type', 'status', 'price', 'currency', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active', 'is_featured', 'is_verified', 'property_type', 'status', 'country', 'city')
    search_fields = ('title', 'description', 'address', 'country__name', 'city__name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PropertyImageInline, PropertyAmenityInline, PropertyTagInline]
    list_per_page = 20
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'property_type', 'status')
        }),
        ('Location', {
            'fields': ('country', 'city', 'address', 'latitude', 'longitude')
        }),
        ('Property Details', {
            'fields': ('price', 'currency', 'bedrooms', 'bathrooms', 'area', 'year_built')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_active', 'is_verified', 'published_at')
        }),
    )


@admin.register(PropertyImage)
class PropertyImageAdmin(ModelAdmin):
    list_display = ('property', 'caption', 'is_primary', 'order', 'created_at')
    list_filter = ('is_primary',)
    search_fields = ('property__title', 'caption')
    list_per_page = 20


@admin.register(PropertyAmenity)
class PropertyAmenityAdmin(ModelAdmin):
    list_display = ('property', 'amenity', 'created_at')
    list_filter = ('amenity__category',)
    search_fields = ('property__title', 'amenity__name')
    list_per_page = 20


@admin.register(PropertyTag)
class PropertyTagAdmin(ModelAdmin):
    list_display = ('property', 'tag', 'created_at')
    search_fields = ('property__title', 'tag__name')
    list_per_page = 20