from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .api.serializers import StudentSerializer

# # Create your views here.

class StudentListView(APIView):
    # model = Student
    # template_name = 'student_list.html'
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response({'students': serializer.data})

    def post(self, request):
        student = request.data.get('students')
        serializer = StudentSerializer(data=student)
        print(student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()

        return Response({"success": "Student '{}' created successfully".format(student_saved.student_name)})

    def put(self, request, pk):
        saved_student = get_object_or_404(Student.objects.all(), pk=pk)
        data = request.data.get('students')
        serializer = StudentSerializer(instance=saved_student, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()

        return Response({"success": f"Student '{student_saved.name}' updated successfully"})


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'student_detail.html'