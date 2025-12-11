from django.urls import path
from . import views



urlpatterns = [
    path("",views.index,name='home'),
    path('post/',views.post,name='post'),
    path('about/',views.about,name='about'),
    path('education/',views.education,name='education'),
    path('experience/',views.experience,name='experience'),
    path('internship/',views.internship,name='internship'),
    path('skill/',views.skill,name='skill'),
    path('project/',views.project,name='project'),
    path('contact/',views.contact,name='contact'),
    path('contactview/',views.contactview,name='contactview'),
    path('404/',views.notfound,name='notfound')
]
