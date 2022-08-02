import django.contrib.auth
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.

def index_view(request):
    return render(request, 'portal/index.html', {'request': request})


@login_required
def logout_view(request):
    django.contrib.auth.logout(request)
    return render(request, 'portal/logout.html')


class Register(generic.CreateView):
    template_name = 'portal/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('portal:index')

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context
