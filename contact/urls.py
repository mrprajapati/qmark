from django.urls import path, include
from .views import contact

urlpatterns = [
    path('', contact, name="contact"),
]
