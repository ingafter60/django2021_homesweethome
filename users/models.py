# USERS/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

	""" Custom User Model """

	# Mendefinisikan daftar of gender
	GENDER_MALE 	= "male"
	GENDER_FEMALE 	= "female"
	GENDER_OTHER 	= "other"

	# Menampilkan daftar gender pada admin panel
	GENDER_CHOICES = (GENDER_MALE, "Male"),(GENDER_FEMALE, "Female"),(GENDER_OTHER, "Other"),


	avatar = models.ImageField(null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
	bio 	 = models.TextField(default="")
