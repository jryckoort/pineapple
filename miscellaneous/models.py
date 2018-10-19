from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    OWNER = 'Chef'
    MEMBER = 'Membre'
    ROLES = (
        (OWNER, 'Chef'),
        (MEMBER, 'Membre'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100,choices=ROLES)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/",max_length=200)

    def __str__(self):
        return self.role
