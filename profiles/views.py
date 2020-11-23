from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import forms, models
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView

from profiles.forms import RegisterForm


User = get_user_model()


class SiteLoginView(LoginView):
    template_name = 'login.html'


# class EditProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'profile.html'
#
# # @login_required
# # def edit_profile_view(request):
# #     return render(request, 'profile.html', {})


class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email']
        )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)


class SiteRegisterOkView(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class SiteLogoutView(LogoutView):
    template_name = 'logout.html'


class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin,  UpdateView):
    template_name = 'profile.html'
    model = User
    fields = ('first_name', 'last_name', 'address', 'year_birth', 'phone_no', 'bank_no')
    success_url = reverse_lazy('profile')
    success_message = "Changes successfully saved"

    def get_object(self, queryset=None):
        return self.request.user




