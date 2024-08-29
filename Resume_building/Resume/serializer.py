from rest_framework import serializers
from .models import UserProfile 

class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=200)
    summary = serializers.CharField(max_length=200)
    education = serializers.CharField(max_length=200)
    skills = serializers.CharField(max_length=200)
    experience = serializers.CharField(max_length=200)
    certifications = serializers.CharField(max_length=200)
    projects = serializers.CharField(max_length=200)
    languages = serializers.CharField(max_length=200)
    hobbies = serializers.CharField(max_length=200)
    phone_number = serializers.IntegerField()
    
    class Meta:
        model = UserProfile
        fields = (
        'name', 'email', 'phone_number', 'address', 'summary', 'education', 'skills', 'experience', 'certifications', 'projects', 'languages', 'hobbies'
        )