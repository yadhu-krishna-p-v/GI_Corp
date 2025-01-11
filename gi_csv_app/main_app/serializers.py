from rest_framework import serializers
from .models import User

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'age']
        
    def validate_name(self, data):
        if len(data) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return data
    
    def validate_email(self, data):
        if data.endswith('.com'):
            return data
        raise serializers.ValidationError("Email must end with .com")
    
    def validate_age(self, data):
        if data < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return data
        
class FileSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    
    def validate_csv_file(self, value):
        if not value.name.endswith('.csv'):
            raise serializers.ValidationError('File is not a CSV')
        return value
        