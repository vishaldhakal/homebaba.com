from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from property.models import Country, City
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blog Categories"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    meta_title = models.CharField(max_length=100, null=True, blank=True)
    meta_description = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="blog_thumbnails/", null=True, blank=True)
    content = HTMLField(
        verbose_name="Blog Content",
        help_text="Use the rich text editor to format your content",
    )
    excerpt = models.TextField(
        max_length=500, blank=True, help_text="A short summary of the blog post"
    )
    
    # Author relationship
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_posts")

    # Category relationships
    categories = models.ManyToManyField(
        "BlogCategory", related_name="posts", blank=True
    )
    
    # Tag relationships
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    # Location relationships
    countries = models.ManyToManyField(Country, related_name="blog_posts", blank=True)
    cities = models.ManyToManyField(City, related_name="blog_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Status fields
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            counter = 1
            self.slug = base_slug
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_comments")
    name = models.CharField(max_length=100, blank=True)  # For non-authenticated users
    email = models.EmailField(blank=True)  # For non-authenticated users
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Comment by {self.author or self.name} on {self.post.title}"
    
    class Meta:
        ordering = ["-created_at"]