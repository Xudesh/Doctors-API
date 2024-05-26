from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIView.as_view())
]