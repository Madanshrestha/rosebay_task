from rest_framework import viewsets

from schools.models import School
from .serializers import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()