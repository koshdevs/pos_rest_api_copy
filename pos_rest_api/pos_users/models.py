from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.conf import settings 
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token 
# Create your models here.

class AccountManager(BaseUserManager):

    def create_user(self,email,username,password=None):

        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save(using=self.db)

        return user
    def create_superuser(self,email,username,password):

        user = self.create_user(
            
            email=self.normalize_email(email),username=username,password=password
            
        )

        user.is_superuser =True # True
        user.is_staff =True # True
        user.is_active =True # True
        user.is_admin = True
        user.save(using=self.db)

        return user 

class Account(AbstractBaseUser):

    email = models.EmailField(max_length=200,verbose_name= 'Email',unique=True) 
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(default=timezone.now,verbose_name= 'Date joined')
    last_login = models.DateTimeField(default=timezone.now,verbose_name= 'Last Login')
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager() #

    def __str__(self):

        return self.email 
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_toke(sender,instance=None,created=False,**kwargs):

    if created:

        Token.objects.create(user=instance)

