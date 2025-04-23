from rest_framework import serializers
from .models import NewHire, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class NewHireSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = NewHire
        fields = ['id', 'name', 'department', 'date_of_hire', 'status', 'role']
