from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Вход',
        'description': 'Авторизация пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация',
        'description': 'Регистрация нового пользователя'
    }
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'title': 'Профиль',
        'description': 'Редактирование пользователя'
    }

    def get_object(self, queryset=None):
        return self.request.user
