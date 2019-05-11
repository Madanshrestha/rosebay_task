from rest_framework import serializers

from students.models import Student
from schools.models import School

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)
    # email = serializers.EmailField()
    school_id = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    
    class Meta:
        model = Student
        print(model.student_name)
        fields = ('student_name', 'email', 'url', 'school_id')

    def create(self, validated_data):
        print(f"hello {validated_data['school_id'].id}")
        validated_data['school_id'] = validated_data['school_id'].id
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student_name = validated_data.get('student_name', instance.student_name)
        instance.email = validated_data.get('email', instance.email)
        instance.school_id = validated_data.get('school_id', instance.school_id)

        instance.save()
        return instance 