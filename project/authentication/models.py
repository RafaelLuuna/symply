from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = {
    'paciente': {
        'friendly_name': 'Paciente',
        'default_page': '/paciente/home/',
    },
    'pscicologo': {
        'friendly_name': 'Pscicólogo',
        'default_page': '/pscicologo/home/',
    },
}

# Create your models here.
class CustomUser(AbstractUser):
    role = models.CharField(
        default='user',
        max_length=50,
        choices=[(role_key, ROLES[role_key]["friendly_name"]) for role_key in ROLES]
    )
    change_password = models.BooleanField(default=False)

