# dictionary/urls.py

from django.urls import path
from .views import WordView
 
urlpatterns = [
    path('', WordView.as_view(), name='all-wrods'),
    path('<word_id>', WordView.as_view(), name='id-word'),
]
