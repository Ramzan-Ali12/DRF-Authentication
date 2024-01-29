from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    # password = models.CharField(max_length=255)
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="authentication_user_groups",
        related_query_name="user",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="authentication_user_permissions",
        related_query_name="user",
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.email
