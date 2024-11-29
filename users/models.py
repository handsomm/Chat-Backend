from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def activate(self, user):
        """
        Activates a user by setting their status to 'active'.
        """
        if user.status != 'active':
            user.status = 'active'
            user.save(using=self._db)
            return user
        return None

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    profile_image = models.URLField(null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('terminated', 'Terminated')
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')

    username = None  # Remove the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Set the custom manager

    def __str__(self):
        return self.email
    def activate(self, user):
        """
        Activates a user by setting their status to 'active'.
        """
        if user.status != 'active':
            user.status = 'active'
            user.save(using=self._db)
            return user
        return None