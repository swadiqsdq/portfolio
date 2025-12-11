from django.urls import path
from . import views 

urlpatterns = [
    path('login/',views.userlogin,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.userLogout,name='logout')
]
