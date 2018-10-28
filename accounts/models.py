from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='Email address',
		max_length=255,
		unique=True
	)

	active = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)  # <- admin user, not super user
	admin = models.BooleanField(default=False)  # <- super user

	# notice the absence of password field
	# that is built in

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []  # <- email and password are required by default

	def get_full_name(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		"""Does the user has a specific permission"""
		return True

	def has_module_perms(self, app_lable):
		"""Does the user has permission to view a specific app"""
		return True

	@property
	def is_staff(self):
		"""Is the user a staff member"""
		return self.staff

	@property
	def is_admin(self):
		"""Is the user a admin member"""
		return self.admin

	@property
	def is_active(self):
		"""Is the user active"""
		return self.active
