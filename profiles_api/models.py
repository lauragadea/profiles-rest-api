from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# all methods defined within the manager can be used to manipulate objects
# within the model that the manager is for
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        # normalize email (set second part all lower case, and first part case sensitive)
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # the password is encripted (converted into a hash and not saved as plain text)
        user.set_password(password)
        # saving object in the db
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = AbstractBaseUser
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # fields that will be in the table
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # model manager that we will use for the objects (so that django cli knows how to create users)
    objects = UserProfileManager()

    # specify a username field bc we are overriding the username that comes by default. We will
    # replace it with our email. When we authenticate user we will provide email and pass
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # as we are defining a method inside a class, we must specify self as first arg
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # similar to toString() in java. So that the object is readable when printing it
    def ___str__(self):
        """Return string representation of our user"""
        return self.email
