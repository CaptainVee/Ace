from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(('email address'), max_length=255, unique=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	admin = models.BooleanField(default=False)

	def __str__(self):
		return f'{ self.user.username } Profile'
		


# class User(AbstractBaseUser):
#   username = models.CharField(('username'), max_length=30, unique=True)
#   first_name = models.CharField(('first name'), max_length=30, blank=True, null=True)
#   last_name = models.CharField(('last name'), max_length=30, blank=True, null=True)
#   email = models.EmailField(('email address'), max_length=255, unique=True)
#   is_staff = models.BooleanField(('staff status'), default=False,
#     help_text=('Designates whether the user can log into this admin site.'))
#   is_active = models.BooleanField(('active'), default=True,
#     help_text=('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
#   date_joined = models.DateTimeField(('date joined'), default=timezone.now)
#   receive_newsletter = models.BooleanField(('receive newsletter'), default=False)
#   birth_date = models.DateField(('birth date'), auto_now=False, null=True)
#   address = models.CharField(('address'), max_length=30, blank=True, null=True)
#   # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#   # phone_number = models.CharField(('phone number'), validators=[phone_regex], max_length=30, blank=True, null=True) # validators should be a list

#   USER_TYPES = (
#     ('Farmer', 'Farmer'),
#     ('Windmill owner', 'Windmill owner'),
#     ('Solar panel owner', 'Solar panel owner'),)
#   user_type = models.CharField(('user type'), choices=USER_TYPES, max_length=30, blank=True, null=True)

#   USERNAME_FIELD = 'username'
#   REQUIRED_FIELDS = ['email',]

#   objects = UserManager()

#   class Meta:
#     verbose_name = ('user')
#     verbose_name_plural = ('users')

#   def get_full_name(self):
#     full_name = '%s %s' % (self.first_name, self.last_name)
#     return full_name.strip()

#   def get_short_name(self):
#     return self.first_name

#   def email_user(self, subject, message, from_email=None):
#     send_mail(subject, message, from_email, [self.email]) 

