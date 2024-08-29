from django.urls import path
from . import views

urlpatterns = [
    path('create_resume/', views.create_resume, name='create_resume'),
    path('resume_created/', views.resume_created, name='resume_created'),
    path('display_resume/', views.display_resume, name='display_resume'),
    path('resume/list', views.UserProfileView.as_view()),
    path('resume/list/delete/<int:id>', views.DeleteView.as_view()),
]
