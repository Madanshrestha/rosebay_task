from rest_framework import serializers
from schools.models import School

class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = ('school_name', 'location', 'url')

    def create(self, validated_data):
        return School.objects.create(**validated_data)
