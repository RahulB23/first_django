from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:user_name>', views.dashboard, name='dashboard'),
]
