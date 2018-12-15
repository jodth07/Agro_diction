# users/urls.py
 
from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create-user"),
    path('login/', authenticate_user),
    path('reup/', UserRetrieveUpdateAPIView.as_view(), name="update-user")
]
