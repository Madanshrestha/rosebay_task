from rest_framework import serializers

from students.models import Student
from schools.models import School

class StudentSerializer(serializers.ModelSerializer):
    school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    
    class Meta:
        model = Student
        print(model.student_name)
        fields = ('student_name', 'email', 'url', 'school_id')

    def create(self, validated_data):
        print(f"hello {validated_data['school_id'].id}")
        validated_data['school_id'] = validated_data['school_id'].id
        return Student.objects.create(**validated_data)