from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.urls import reverse


# Create your views here.

def index_view(request):
    return render(request, 'portal/index.html')


class Register(generic.CreateView):
    template_name = 'portal/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse('portal:index')
