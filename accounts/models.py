from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,password=None):
        if not email:
            raise ValueError('Users must have an email')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
            
            
    
    
class MyUser(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True,verbose_name='email address')
    first_name  = models.CharField(max_length=255, blank=True)
    last_name   = models.CharField(max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)

    
    objects = MyUserManager()
    
    REQUIRED_FIELDS = ['first_name', 'last_name',]
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_short_name(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    
    @property
    def is_staff(self):
        return self.is_admin
    


