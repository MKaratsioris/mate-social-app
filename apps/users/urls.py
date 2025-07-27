from django.urls import path
from django.contrib.auth import views as auth_views

from apps.users import views as users_views
from apps.users.forms import MateAuthenticationForm

urlpatterns = [
    path("home/<user_id>", users_views.home, name="home"),
    path('signin', users_views.signin, name='signin'),
    path('login', 
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=MateAuthenticationForm
        ), 
        name='login'
    ),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]