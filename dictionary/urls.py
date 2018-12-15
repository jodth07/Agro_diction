# dictionary/urls.py
from rest_framework_mongoengine import routers as routers

from django.urls import path
from .views import WordView

router = routers.DefaultRouter()
router.register(r'dictionary', WordView)

 
urlpatterns = [
] 

urlpatterns += router.urls