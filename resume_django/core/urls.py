from django.urls import path
from . import views
from . import views_extended

app_name='core'
urlpatterns = [
    #path('profiles/create/',views.CreateApplicantAPIView.as_view(),name="profile_list"),
    path('education/',views_extended.EducationAPIView.as_view(),name="education"),
    path('education/<int:id>',views_extended.EducationDetailAPIView.as_view(),name="education"),
    path('experience/',views_extended.ExperienceAPIView.as_view(),name="experience"),
    path('experience/<int:id>',views_extended.ExperienceDetailAPIView.as_view(),name="experience"),
    path('project/',views_extended.ProjectAPIView.as_view(),name="project"),
    path('project/<int:id>',views_extended.ProjectDetailAPIView.as_view(),name="project"),
    path('certification/',views_extended.CertificationAPIView.as_view(),name="certification"),
    path('certification/<int:id>',views_extended.CertificationDetailAPIView.as_view(),name="certification"),
    path('achievement/',views_extended.AchievementAPIView.as_view(),name="achievement"),
    path('achievement/<int:id>',views_extended.AchievementDetailAPIView.as_view(),name="achievement"),

    path('resumes/',views.ResumeAPIView.as_view(),name="resume"),
    path('resumes/<int:id>',views.ResumeDetailAPIView.as_view(),name="resume"),
    path('applicant/',views.ApplicantAPIView.as_view(),name="profiles"),
    path('applicant/<int:id>',views.ApplicantDetailAPIView.as_view(),name="profile"),
    path('skills/',views.SkillAPIView.as_view(),name="skills"),
    path('skills/<int:id>',views.SkillDetailAPIView.as_view(),name="skill"),
]

