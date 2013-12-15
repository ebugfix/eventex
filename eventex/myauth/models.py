# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, cpf, name=None, password=None):
        user = self.model(cpf=cpf, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **credentials):
        return self.create_user(**credentials)


class User(AbstractBaseUser):
    cpf = models.CharField(max_length=11, unique=True, db_index=True)
    name = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'cpf'

    objects = UserManager()
