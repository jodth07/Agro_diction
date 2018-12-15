# images/urls.py

 
from django.urls import path
from rest_framework_mongoengine import routers

from .views import GallerysView
 
router = routers.DefaultRouter()
router.register(r'gallery', GallerysView)


urlpatterns = [
]

urlpatterns += router.urls
