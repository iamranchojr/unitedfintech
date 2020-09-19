from rest_framework import serializers
from app.models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'telephone',
            'address',
            'salary'
        ]
