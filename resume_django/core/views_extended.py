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
EducationAPIView handles get and post requests
On get request it returns List of Educations
On post request it accepts data of new Education

also the in post request it should have a field with name curriculumVitae
 with the value of file to be uploaded
'''
class EducationAPIView(ListCreateAPIView):
    serializer_class=EducationSerializer
    queryset=Education.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','degreeName','major','collegeName','endYear',]
    filterset_fields=['id','degreeName','major','collegeName','startYear','endYear',]
    Ordering_fields=['id','degreeName','major','collegeName','startYear','endYear',]

'''
EducationDetailAPIView handles get,put and delete requests
it gets id from Education/<int:id>
On get request it returns Education with given id
On put request it updates Education with given id
On delete request it deletes data of the Education
'''
class EducationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=EducationSerializer
    lookup_field='id'
    queryset=Education.objects.all()

'''
EducationAPIView handles get and post requests
On get request it returns List of Educations
On post request it accepts data of new Education

also the in post request it should have a field with name curriculumVitae
 with the value of file to be uploaded
'''
class ExperienceAPIView(ListCreateAPIView):
    serializer_class=ExperienceSerializer
    queryset=Experience.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','position','institutionName','endDate','work',]
    filterset_fields=['id','position','institutionName','startDate','endDate','work']
    Ordering_fields=['id','position','institutionName','startDate','endDate','work']

'''
EducationDetailAPIView handles get,put and delete requests
it gets id from Education/<int:id>
On get request it returns Education with given id
On put request it updates Education with given id
On delete request it deletes data of the Education
'''
class ExperienceDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ExperienceSerializer
    lookup_field='id'
    queryset=Experience.objects.all()

'''
EducationAPIView handles get and post requests
On get request it returns List of Educations
On post request it accepts data of new Education

also the in post request it should have a field with name curriculumVitae
 with the value of file to be uploaded
'''
class ProjectAPIView(ListCreateAPIView):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','name','endDate','work',]
    filterset_fields=['id','name','startDate','endDate','work']
    Ordering_fields=['id','name','startDate','endDate','work']

'''
EducationDetailAPIView handles get,put and delete requests
it gets id from Education/<int:id>
On get request it returns Education with given id
On put request it updates Education with given id
On delete request it deletes data of the Education
'''
class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectSerializer
    lookup_field='id'
    queryset=Project.objects.all()

'''
CertificationAPIView handles get and post requests
On get request it returns List of eesumes
On post request it accepts data of new Certification
'''
class CertificationAPIView(ListCreateAPIView):
    serializer_class=CertificationSerializer
    queryset=Certification.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','name','certificationId','issuingAthority','issueDate']
    filterset_fields=['id','name','certificationId','issuingAthority','issueDate']
    Ordering_fields=['id','name','certificationId','issuingAthority','issueDate']

'''
CertificationDetailAPIView handles get,put and delete requests 
it gets id from Certifications/<int:id>
On get request it returns Certification with given id
On put request it updates Certification with given id
On delete request it deletes data of the Certification
'''
class CertificationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=CertificationSerializer
    lookup_field='id'
    queryset=Certification.objects.all()

'''
AchievementAPIView handles get and post requests
On get request it returns List of eesumes
On post request it accepts data of new Achievement
'''
class AchievementAPIView(ListCreateAPIView):
    serializer_class=AchievementSerializer
    queryset=Achievement.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['id','name',]
    filterset_fields=['id','name',]
    Ordering_fields=['id','name',]

'''
AchievementDetailAPIView handles get,put and delete requests 
it gets id from Achievements/<int:id>
On get request it returns Achievement with given id
On put request it updates Achievement with given id
On delete request it deletes data of the Achievement
'''
class AchievementDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=AchievementSerializer
    lookup_field='id'
    queryset=Achievement.objects.all()

""" '''
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
    queryset=Profile.objects.all() """