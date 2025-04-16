from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Blog Category URLs
    path('categories/', views.BlogCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<slug:slug>/', views.BlogCategoryDetailView.as_view(), name='category-detail'),
    
    # Tag URLs
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<slug:slug>/', views.TagDetailView.as_view(), name='tag-detail'),
    
    # Blog Post URLs
    path('posts/', views.BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    
    # Comment URLs
    path('posts/<slug:post_slug>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<slug:post_slug>/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
] 