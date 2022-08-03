from django.urls import path
from .views import *

app_name = 'portal'
urlpatterns = [
    path('', index_view, name='index'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_form, name='login'),
    path('contactus/', contact_us_form, name='contactus'),
    path('profile/', profile_view, name='profile'),
    path('settings/', Settings.as_view(), name='settings'),
    path('panel/', UserPanelView.as_view(), name='panel'),
    path('create_course/',CreateCourse.as_view(),name='create_course')
]
