
from rest_framework import routers
from django.urls import path,include
from accounts.viewsets import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

router = routers.DefaultRouter()
router.register(r'^', "Accounts")

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]