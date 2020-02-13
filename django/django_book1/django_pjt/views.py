from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = 'home.html'

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTemplateView(generic.TemplateView):
    template_name = 'registration/register_done.html'