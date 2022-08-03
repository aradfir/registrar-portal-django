import django.contrib.auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import LoginForm, ContactForm, RegisterForm, SettingsForm, CourseCreateForm
from .models import Course
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index_view(request):
    return render(request, 'portal/index.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'portal/logout.html')


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
                return render(request, 'portal/login.html',
                              {'form': form, 'invalid_prev_login': True})
    else:
        form = LoginForm()
    return render(request, 'portal/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, "portal/profile.html")


@require_http_methods(['POST', 'GET'])
def contact_us_form(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            message = f"SENDER EMAIL:{form.cleaned_data.get('email')}\nSENDER TEXT:\n" \
                      f"{form.cleaned_data.get('text')}"
            subject = form.cleaned_data.get('form_title')
            email_from = settings.EMAIL_HOST_USER

            send_mail(subject, message, email_from, settings.EMAIL_RECIPIENT)
            return render(request, 'portal/contact_success.html')
        else:
            return render(request, 'portal/contact_us.html',
                          {'form': form, 'invalid_prev_fill': True})
    else:
        form = ContactForm()
    return render(request, 'portal/contact_us.html', {'form': form})


class Settings(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = 'portal/show_form.html'
    model = User
    form_class = SettingsForm
    success_url = reverse_lazy('portal:profile')

    def get_object(self, queryset=None):
        return self.request.user


class Register(generic.CreateView):
    template_name = 'portal/show_form.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('portal:index')


from .mixins import SuperUserRequiredMixin


class CreateCourse(SuperUserRequiredMixin, generic.CreateView):
    template_name = 'portal/show_form.html'
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('portal:panel')


def user_panel(request):
    return render(request, 'portal/panel.html')


class UserPanelView(generic.ListView):
    model = Course
    template_name = 'portal/panel.html'
    context_object_name = 'courses'
