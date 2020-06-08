from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cat_name
    
    
class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    img  = models.ImageField(upload_to='post_pics')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=User.id)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class BlogComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=User.id)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
class Reader(models.Model):
    email = models.EmailField(max_length=100)
    registered_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    
    

    