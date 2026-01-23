from django.urls import path
from .views import CompareAPIView

urlpatterns = [
    path("compare/", CompareAPIView.as_view(), name="compare"),
]