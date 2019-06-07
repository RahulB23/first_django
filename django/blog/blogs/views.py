from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Blog_Post
from django.template import RequestContext

def homepage(request):
    blog_list = Blog_Post.objects.order_by('-user')[:5]
    output = {'blog_list': blog_list}
    return render(request, 'blogs/homepage.html', output)


def dashboard(request, user_name):
    object = User.objects.get(username=user_name)
    blog_list2 = Blog_Post.objects.filter(user = object.id)
    output2 = {'blog_list2': blog_list2}
    return render(request, 'blogs/dashboard.html', output2, {'name': [' user_name']})
