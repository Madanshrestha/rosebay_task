from rest_framework import serializers

from .models import School

class SchoolSerializer(serializers.Serializer):
    school_name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return School.objects.create(**validated_data)