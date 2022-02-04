from django.urls import path
from email_verification import views

urlpatterns = [
    path('register', views.register_attempt, name="register_attempt"),
    path('', views.login_attempt,
         name="login_attempt"),
    path('token/', views.token_send, name="token_send"),
    path('success/', views.success, name='success'),
    path('verify/<auth_token>/', views.verify, name="verify"),
    path('error', views.error_page, name="error"),
    path('forget-password/', views.ForgetPassword, name="forget_password"),
    path('change-password/<token>/', views.ChangePassword,
         name="change_password"),
    path('logout', views.log_out, name='logout'),
]
