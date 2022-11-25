from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status,filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
'''
ApplicantAPIView handles get and post requests
On get request it returns List of applicants
On post request it accepts data of new applicant

also the in post request it should have a field with name curriculumVitae
 with the value of file to be uploaded
'''
class ApplicantAPIView(ListCreateAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','name','email','contact','about','headline']
    filterset_fields=['id','name','email','contact','about','headline',]
    Ordering_fields=['id','name','email','contact','about','headline',]

'''
ApplicantDetailAPIView handles get,put and delete requests
it gets id from applicant/<int:id>
On get request it returns applicant with given id
On put request it updates applicant with given id
On delete request it deletes data of the applicant
'''
class ApplicantDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProfileSerializer
    lookup_field='id'
    queryset=Profile.objects.all()

'''
ResumeAPIView handles get and post requests
On get request it returns List of eesumes
On post request it accepts data of new resume
'''
class ResumeAPIView(ListCreateAPIView):
    serializer_class=ResumeSerializer
    queryset=Resume.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','applicant','datetime']
    filterset_fields=['id','applicant','datetime']
    Ordering_fields=['id','applicant','datetime']

'''
ResumeDetailAPIView handles get,put and delete requests 
it gets id from resumes/<int:id>
On get request it returns resume with given id
On put request it updates resume with given id
On delete request it deletes data of the resume
'''
class ResumeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ResumeSerializer
    lookup_field='id'
    queryset=Resume.objects.all()

'''
SkillAPIView handles get and post requests
On get request it returns List of skill
On post request it accepts data of new skill
'''
class SkillAPIView(ListCreateAPIView):
    serializer_class=SkillSerializer
    queryset=Skill.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','name']
    filterset_fields=['id','name']
    Ordering_fields=['id','name']

'''
SkillDetailAPIView handles get,put and delete requests 
it gets id from skills/<int:id>
On get request it returns skill with given id
On put request it updates skill with given id
On delete request it deletes data of the skill
'''
class SkillDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=SkillSerializer
    lookup_field='id'
    queryset=Profile.objects.all()