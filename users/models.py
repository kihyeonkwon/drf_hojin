from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            is_admin=is_admin,
            is_staff=is_staff,
            is_active=is_active,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True,
        )
        # user.save(using=self._db)
        return user





class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    # user.following -> 내가 팔로우하고 있는 유저들을 갖고옴
    # user.followers -> 나를 팔로우하고 있는 유저들을 갖고옴

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email + "유저입니다"
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    @is_staff.setter
    def is_staff(self, value):
        self.is_admin = value
    


