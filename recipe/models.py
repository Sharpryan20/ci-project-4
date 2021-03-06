from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_post")
    updated_on = models.DateTimeField(auto_now=True)
    preparation_length = models.CharField(max_length=15, default=0)
    cooking_time = models.CharField(max_length=15, default=0)
    total_time = models.CharField(max_length=15, default=0)
    serving_size = models.CharField(max_length=15, default=0)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        """
        Shows order of posts.
        """
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.title} | {self.author}"

    def number_of_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """
        Show order of comments.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
