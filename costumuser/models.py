# from time import timezone
#
# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
#
# class CustomUserManager(BaseUserManager):
#     def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):
#         now = timezone.now()
#         if not email:
#             raise ValueError('you need email')
#         email = self.normalize_email(email)
#         user = self.model(email=email,is_staff=is_staff,is_active=True,
#                           is_superuser=is_superuser,last_login=now,
#                           date_joined=now,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self,email,password=None,**extra_fields):
#         return self._create_user(email,password,False,False,**extra_fields)
#
#     def create_superuser(self,email,password=None,**extra_fields):
#         return self._create_user(email,password,True,True,**extra_fields)
#
#
# class CostumUser(AbstractBaseUser):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     numero = models.IntegerField(unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email','username']
#     objects = CustomUserManager()
