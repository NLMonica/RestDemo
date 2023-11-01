
from django.urls import path, include

from .views import (
    rest_api_views,
)

urlpatterns = [
    path('api', rest_api_views.as_view()),
    path('api/<int:id>/', rest_api_views.as_view()),
]