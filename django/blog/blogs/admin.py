from django.contrib import admin

# Register your models here.
from .models import User, Blog_Post

admin.site.register(User)
admin.site.register(Blog_Post)
