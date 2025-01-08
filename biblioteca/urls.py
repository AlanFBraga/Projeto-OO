# biblioteca/urls.py

from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('livros/', include('livros.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
