from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class Blog_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_text = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_text
