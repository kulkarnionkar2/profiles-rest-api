from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionError
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Managger For User Profiles"""

    def create_user(self, email, name, password=None):
        #Here password is = None since Django gives error if we left password field empty and could accept any non-null value so it's just check for non_null
        """Create a new user profile"""
        if not email:
            raise ValueError(' User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """ create a new superuser with given details"""
        user = self.create_user(email,name,password)


        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionError):
    """  Database model for the users in system   """
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active =models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """ Retrive full name of user """
        return self.name
    
    def get_short_name(self):
        """ Retrive short name of the user"""
        return self.name
    
    def __str__(self) -> str:
        """ Return String representation of our user """
        return self.email