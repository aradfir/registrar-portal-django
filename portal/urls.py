from django.urls import path
from .views import *

app_name = 'portal'
urlpatterns = [
    path('', index_view, name='index'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_form, name='login'),
]
