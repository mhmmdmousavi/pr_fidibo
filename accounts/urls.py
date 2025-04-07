from .views import hello_response
from django.urls import path


urlpatterns = [
    path('', hello_response),
]