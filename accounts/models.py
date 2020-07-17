from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class MyAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email Require')
        if not name:
            raise ValueError('Name Require')
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, name, email, password=None):
    #     user = self.create_user(
    #         name=name,
    #         email=email,
    #         password=password
    #     )
    #     user.is_staff = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email=email, password=password, name=name)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=60, null=False, verbose_name='name')
    email = models.EmailField(
        max_length=60, unique=True, null=False, verbose_name='email')
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.name

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff

    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin

    # @property
    # def is_superuser(self):
    #     "Is the user a admin member?"
    #     return self.admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active
