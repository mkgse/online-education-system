from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    #create and saves an User with the given email and password.
    def create_user(self,username,first_name,last_name,email,password=None):

       if not email:
           raise ValueError("User must have an valid email address")
       if not username:
            raise ValueError("User must have an username")
       user = self.model(email = self.normalize_email(email),
       username = username,
       first_name = first_name,
       last_name = last_name
       )
       user.set_password(password)
       user.save(using=self._db)
       return user
    
    def create_superuser(self,username,first_name,last_name,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
    
#Create and saves a superuser with the given email and password.
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
            )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50,unique=True)
    phone_number = models.CharField(max_length=50)
    #require
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()
    
    def __str__(self):
        return self.email
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def has_perm(self,perm,obj=None):
        "Does the user have a specific permissiom?"
        #Only Superuser have permission to access all data
        return self.is_admin
    
    def has_module_perms(self,add_label):
        "Does the user have permission to view the app `app_label`?"
        return True
