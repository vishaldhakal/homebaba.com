from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import BlogCategory, BlogPost, Tag, Comment
from tinymce.widgets import TinyMCE
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    form = BlogForm
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_published', 'is_featured', 'views_count')
    list_filter = ('is_published', 'is_featured', 'categories', 'tags', 'countries', 'cities', 'created_at')
    search_fields = ('title', 'content', 'excerpt', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'tags', 'countries', 'cities')
    date_hierarchy = 'created_at'
    readonly_fields = ('views_count', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'thumbnail', 'content', 'excerpt')
        }),
        ('SEO Information', {
            'fields': ('meta_title', 'meta_description')
        }),
        ('Categorization', {
            'fields': ('categories', 'tags')
        }),
        ('Location', {
            'fields': ('countries', 'cities')
        }),
        ('Status', {
            'fields': ('is_published', 'is_featured')
        }),
        ('Statistics', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('post', 'author', 'name', 'email', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('content', 'name', 'email')
    readonly_fields = ('created_at', 'updated_at')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"
