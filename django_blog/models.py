from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank = True, upload_to = 'post_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('django_blog:post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('django_blog:blog-home')
        
