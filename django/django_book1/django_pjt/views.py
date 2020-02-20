from django.views import generic
from django.contrib.auth import (forms, mixins)
from django.urls import reverse_lazy


class HomeView(generic.TemplateView):
    template_name = 'home.html'

class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTemplateView(generic.TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(mixins.AccessMixin):
    raise_exception = True
    permission_denied_message = 'Owner only can update/delete the object'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
