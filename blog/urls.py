from django.urls import path
from .views import blog, ContactoVista



urlpatterns = [
    path('blog/', blog, name='blog'),
]

