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
        slug_field='position'
    )
    projects = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Project.objects.all(),
        slug_field='name'
    )
    education = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Education.objects.all(),
        slug_field='collegeName'
    )
    certifications = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Certification.objects.all(),
        slug_field='name'
    )
    achieveements = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Achievement.objects.all(),
        slug_field='name'
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
