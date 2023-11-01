from rest_framework import serializers
from .models import REST

class REST_Serializer(serializers.ModelSerializer):
    class Meta:
        model = REST
        fields = ["roll", "student_name", "admission_date", "user"]