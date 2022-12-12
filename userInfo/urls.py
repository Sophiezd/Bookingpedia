from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path('redirect', views.login_redirect, name='login_redirect'),
]