from rest_framework import serializers
from .models import User, CompanyProfile, EmployeeProfile
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_active', 'is_verified', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True} 
        }

    def create(self, validated_data):
        email_domain = validated_data['email'].split('@')[-1].lower()
        common_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        
        # Set role based on the email domain
        if email_domain in common_domains:
            validated_data['role'] = User.RoleChoices.USER
        else:
            validated_data['role'] = User.RoleChoices.AGENCY

        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'
