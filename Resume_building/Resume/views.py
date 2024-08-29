from django.shortcuts import render, redirect
from .forms import UserProfileForm
from rest_framework.views import APIView
from .models import UserProfile
from .serializer import UserProfileSerializer
from django.http import HttpResponseNotAllowed
from rest_framework.response import Response
from rest_framework import status

def create_resume(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():                                                                                                                                                                         
            form.save()
            return redirect('display_resume')  # Redirect to a success page
    else:
        form = UserProfileForm()
    return render(request, 'create_resume.html', {'form': form})

def resume_created(request):
    return render(request, 'resume_created.html')

class UserProfileView(APIView):
    def get(self, request,*args, **kwargs):
            result = UserProfile.objects.all()
            serializers = UserProfileSerializer(result, many = True)
            return Response({'status': 'success', "Resumes": serializers.data}, status=200)
        
class DeleteView(APIView):
    def delete(self, request, id):
        UserProfile.objects.all().delete()
        return Response({'status': 'success','message': 'Student record deleted successfully'},status=status.HTTP_200_OK)

def display_resume(request):
    if request.method == 'GET':
        # Assuming there's only one resume in the database
        resume = UserProfile.objects.last()
        return render(request, 'display-resume.html', {'resume': resume})
    else:
        # Handle other HTTP methods if needed
        return HttpResponseNotAllowed(['GET'])
