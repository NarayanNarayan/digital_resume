from django.urls import path
from . import views
from . import views_extended

app_name='core'
urlpatterns = [
    #path('profiles/create/',views.CreateApplicantAPIView.as_view(),name="profile_list"),
    path('education/',views_extended.EducationAPIView.as_view(),name="education"),
    path('education/<int:id>',views_extended.EducationDetailAPIView.as_view(),name="education"),

    path('resumes/',views.ResumeAPIView.as_view(),name="resume"),
    path('resumes/<int:id>',views.ResumeDetailAPIView.as_view(),name="resume"),
    path('applicant/',views.ApplicantAPIView.as_view(),name="profiles"),
    path('applicant/<int:id>',views.ApplicantDetailAPIView.as_view(),name="profile"),
    path('skills/',views.SkillAPIView.as_view(),name="skills"),
    path('skills/<int:id>',views.SkillDetailAPIView.as_view(),name="skill"),
]

