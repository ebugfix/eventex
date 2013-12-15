# coding: utf-8
from django.contrib.auth import get_user_model


class EmailBackend(object):
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        if email is None:
            email = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel.objects.get(email=email)
        except (UserModel.DoesNotExist,
                UserModel.MultipleObjectsReturned):
            return None

        if not user.check_password(password):
            return None
        return user
