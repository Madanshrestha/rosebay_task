from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import School
from .serializers import SchoolSerializer
# Create your views here.

class SchoolView(APIView):
    
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)

        return Response({"schools": serializer.data})

    def post(self, request):
        school = request.data.get("schools")
        serializer = SchoolSerializer(data=school)
        
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()

        return Response({"success": f"School '{student_saved.school_name}' created successfully"})
