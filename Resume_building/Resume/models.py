from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    summary = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    certifications = models.TextField()
    projects = models.TextField()
    languages = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        return self.name

