from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, RegisterView, ProfileView, generate_new_password, activate_new_user

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/generatepassword/', generate_new_password, name='generate_new_password'),
    path('activate/<int:pk>/', activate_new_user, name='activate_new_user')
]
