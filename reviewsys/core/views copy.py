from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView
# Create your views here.
class CreateApplicantAPIView(CreateAPIView):
    serializer_class=ProfileSerializer

class ApplicantListAPIView(ListAPIView):
    serializer_class=ProfileSerializer
    #queryset=Profile.objects.all()
    def get_queryset(self):
        return Profile.objects.all()

def home(request):
    person=Profile.objects.get(id=12)
    print(person.skills.all())
    context={}
    return render(request,"home.html",context)
class HomeView(View):
    def get(self,request,*args,**kwargs):
        person=Profile.objects.get(id=12)
        print(person.skills)
        context={}
        return render(request,"home.html",context)

def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles,many=True)
    return JsonResponse(serializer.data,safe=False)
def profile(request,id):
    profile = Profile.objects.get(pk=id)
    serializer = ProfileSerializer(profile)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET','POST'])
def skill_list(request):
    if request.method=='GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills,many=True)
        print(serializer.data)
        return Response({'data':serializer.data})
    if request.method=='POST':
        serializer = SkillSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def skill_detail(request,id):
    try:
        skill= Skill.objects.get(pk=id)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer = SkillSerializer(skill,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)