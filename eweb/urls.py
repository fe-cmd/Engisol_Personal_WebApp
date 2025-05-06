from django.urls import path
from .import views
from .views import RequestPasswordResetEmail, VerificationView, EmailValidationView, UsernameValidationView, CompletePasswordReset, \
IndexView, TechView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('index', IndexView.as_view(), name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('tech', TechView.as_view(), name='tech'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('password_reset_form', RequestPasswordResetEmail.as_view(), name='password_reset_form'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('set-new-password/<uidb64>/<token>',csrf_exempt(CompletePasswordReset.as_view()), name='reset_user_password')
]
