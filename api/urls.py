from django.contrib import admin
from django.urls import path, include

from rest_framework_mongoengine import routers as merouters
from .views import ToolViewSet, ContactsView, PostSerializerView

merouter = merouters.DefaultRouter()
merouter.register(r'mongo', ToolViewSet)

urlpatterns = [
    path('contacts/<int:contact_id>', ContactsView.as_view(), name='id-contacts'),
    path('users/', include('users.urls')),
    path('dictionary/', include('dictionary.urls')),
    path('contacts/', ContactsView.as_view(), name='all-contacts'),
    path('posts/', PostSerializerView.as_view(), name='all-posts'),
]


urlpatterns += merouter.urls


 
