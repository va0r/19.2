from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
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

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Регистрация на сайте',
            message='Вы успешно зарегистрировались на сайте "КАТАЛОГ"',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    extra_context = {
        'title': 'Профиль',
        'description': 'Редактирование пользователя'
    }

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def generate_new_password(request):
    def generate_alphanum_crypt_string(length):
        import secrets
        import string
        letters_and_digits = string.ascii_letters + string.digits
        crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for _ in range(length))
        return crypt_rand_string

    new_password = generate_alphanum_crypt_string(16)
    request.user.set_password(new_password)
    request.user.save()

    send_mail(
        subject='Пароль изменён!',
        message=f'Вы успешно сменили пароль на сайте "КАТАЛОГ". Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    del new_password

    return redirect(reverse('users:login'))


def activate_new_user(request, pk):
    user = get_user_model()
    user_for_activate = user.objects.get(id=pk)
    user_for_activate.is_active = True
    user_for_activate.save()
    return render(request, 'users/activate_user.html')
