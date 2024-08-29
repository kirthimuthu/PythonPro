from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone_number', 'address', 'summary', 'education', 'skills', 'experience', 'certifications', 'projects', 'languages', 'hobbies']
