from django.urls import path
from .views import CustomLoginView, signup

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
]
