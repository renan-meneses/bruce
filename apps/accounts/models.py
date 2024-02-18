from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _create_user(
        self, name, email, password, surname, **extra_fields
    ):
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            surname = surname,
            password = password,
            **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_superuser(self,name, email=None, password=None, surname=None, **extra_fields):
        user = self._create_user(
           name, email, password, surname, **extra_fields
        )
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(_("name"), max_length=50)
    surname = models.CharField(_("surname"), max_length=50)
    email = models.EmailField(_("email address"), max_length=95, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.full_name
