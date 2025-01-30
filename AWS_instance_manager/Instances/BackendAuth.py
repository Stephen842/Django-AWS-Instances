from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import MyUser

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        try:
            if email:
                user = MyUser.objects.get(email=email)
            else:
                user = MyUser.objects.get(username=username)
            if user and user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None