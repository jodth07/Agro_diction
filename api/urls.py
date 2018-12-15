from django.contrib import admin
from django.urls import path, include

from rest_framework_mongoengine import routers as routers
from .views import ToolViewSet, ContactsView, PostSerializerView

router = routers.DefaultRouter()
router.register(r'tool', ToolViewSet)

urlpatterns = [
    path('contacts/<int:contact_id>', ContactsView.as_view(), name='id-contacts'),
    path('users/', include('users.urls')),
    path('dictionary/', include('dictionary.urls')),
    path('contacts/', ContactsView.as_view(), name='all-contacts'),
    path('posts/', PostSerializerView.as_view(), name='all-posts'),
    path('medias/', include('images.urls'))
]


urlpatterns += router.urls


 
