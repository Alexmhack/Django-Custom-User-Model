from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widgets=forms.PasswordInput)
	password2 = forms.CharField(widgets=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)

	def clean_email(self):
		"""check if the email already exists"""
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise ValidationError('email already exists')
		return email

	def clean_password(self):
		"""check if the both passwords match"""
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('passwords don\'t match')
		return password2
