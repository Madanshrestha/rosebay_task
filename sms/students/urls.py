from django.urls import path, include

from .api.viewsets import StudentViewSet

app_name = 'students'

urlpatterns = [
    path('students/', StudentViewSet.as_view({'get': 'list'})),
]
