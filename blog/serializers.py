from rest_framework import serializers
from .models import BlogCategory, BlogPost, Tag, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'description']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'name', 'email', 'content', 'created_at', 'updated_at', 'is_approved']
        read_only_fields = ['created_at', 'updated_at', 'is_approved']


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = BlogCategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'meta_title', 'meta_description', 'thumbnail', 
            'content', 'excerpt', 'author', 'categories', 'tags', 'countries', 
            'cities', 'created_at', 'updated_at', 'is_featured', 'is_published', 
            'views_count', 'comments'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'views_count'] 