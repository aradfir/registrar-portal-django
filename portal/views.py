import django.contrib.auth
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index_view(request):
    return render(request, 'portal/index.html', {'request': request})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'portal/logout.html',{'request':request})


@require_http_methods(['POST', 'GET'])
def login_form(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_to=reverse_lazy('portal:index'))
            else:
                return render(request,'portal/login.html',{'form':form,'request':request,'invalid_prev_login':True})
    else:
        form = LoginForm()
    return render(request, 'portal/login.html', {'form': form,'request':request})


class Register(generic.CreateView):
    template_name = 'portal/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('portal:index')

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context
