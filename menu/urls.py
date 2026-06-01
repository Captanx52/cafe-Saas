from django.urls import path
from .views import MenuAPIView


urlpatterns = [
    path('', MenuAPIView.as_view()),
]