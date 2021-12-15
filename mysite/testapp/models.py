from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User, UserManager

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


STATUS = (
    (0,"Empty"),
    (1,"Occuped")
)

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='testapp_tasks')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    parking_lot_number = models.IntegerField(unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


