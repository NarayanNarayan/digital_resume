from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register([Skill, Profile, Experience, Project,
                     Education, Certification, Achievement,Resume])
