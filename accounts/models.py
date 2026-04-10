from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password

phone_validator = RegexValidator(
    regex='\^d{11}$',
    message = ("phone number must be 11 digits")
)

pin_validator = RegexValidator(
    regex='\^d{4}$',
    message = ("trxns pin must be 4 digits")
)


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_feilds):
        if not email:
            raise ValueError("Gmail is required!")
        if not phone_number:
            raise ValueError("Phone number is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_feilds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone_number, password=None, **extra_feilds):
        extra_feilds.setdefault('is_staff', True)
        extra_feilds.setdefault('is_superuser', True)
        extra_feilds.setdefault('is_active', True)
        #if extra_feilds.get('is_staff') is not True:
            #raise ValueError("Superuser must have is_staff=True.")
        #if extra_feilds.get('is_superuser') is not True:
         #   raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, phone_number, password, **extra_feilds)
    
class Costomer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\d{11}$', message="Phone number must be entered in the format: '08012345678'. and 11 digits.")
    pin_validator = RegexValidator(regex=r'^\d{4}$', message="PIN must be entered in the format: '1234'. Exactly 4 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True)
    
    transaction_pin = models.CharField(
        max_length=128,
      #  validators=[pin_validator],
        null=True,
        blank=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()
    
    def set_transaction_pin(self, raw_pin):
        self.transaction_pin = make_password(raw_pin)
        self.save()

    def verify_transaction_pin(self, raw_pin):
        return check_password(raw_pin, self.transaction_pin)
        #user.save()
    def __str__(self):
        return self.email
    #phone_number = models.DecimalField(max_length=11)






# Create your models here.
