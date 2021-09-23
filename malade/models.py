#from typing_extensions import Required
from django.db import models

from datetime import date, time, datetime

from phone_field import PhoneField
from django.urls import reverse

# Create your models here.


class Malade(models.Model):
    profile = models.ImageField(upload_to = "profile_all")

    nom = models.CharField(max_length=100)

    prenom = models. CharField(max_length=50)

    email = models.EmailField()

    phone = PhoneField(blank=True,unique=True, help_text='Contact phone number')

    maladie = models.CharField(max_length=200)

    date_heur_A = models.DateTimeField()

    date_heur_d = models.DateTimeField(auto_now_add=False, auto_now=False)

    description = models.TextField()

    def get_absolute_url(self):
        return reverse("/",kwargs={"pk":self.pk})