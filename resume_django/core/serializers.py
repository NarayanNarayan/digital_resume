from rest_framework import serializers
from .models import *
'''
ProfileSerializer
'''


class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Skill.objects.all(),
        slug_field='name'
    )
    experiences = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Experience.objects.all(),
        slug_field='id'
    )
    projects = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Project.objects.all(),
        slug_field='id'
    )
    education = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Education.objects.all(),
        slug_field='id'
    )
    certifications = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Certification.objects.all(),
        slug_field='id'
    )
    achieveements = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Achievement.objects.all(),
        slug_field='id'
    )
    """ experiences=serializers.StringRelatedField(many=True)    
    projects=serializers.StringRelatedField(many=True)
    education=serializers.StringRelatedField(many=True)
    certifications=serializers.StringRelatedField(many=True)
    achieveements=serializers.StringRelatedField(many=True) """
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'headline', 'contact', 'dob', 'address', 'pin', 'city', 'state', 'country', 'pic', 'github', 'linkedin', 'website', 'about', 'interests', 'summary', 'vision', 'ideas',
                  'skills',
                  'experiences',
                  'projects',
                  'education',
                  'certifications',
                  'achieveements']


class ResumeSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Resume
        fields = ['id', 'applicant', 'file', 'datetime']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class ExperienceSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Experience
        fields = ['id','applicant','id','institutionName','startDate','endDate','work']
class EducationSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Education
        fields = ['id', 'applicant','degreeName','major','collegeName','startYear','endYear']

class ProjectSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Project
        fields = ['id','applicant','name','startDate','endDate','work' ]

class CertificationSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Certification
        fields = ['id','applicant','name','certificationId','issuingAthority','issueDate']


class AchievementSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(
        queryset=Profile.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Achievement
        fields = ['id','applicant', 'name']