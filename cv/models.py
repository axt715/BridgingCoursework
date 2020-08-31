from django.db import models
from django.utils import timezone

class PersonalDetails(models.Model):
    firstName = models.CharField(default='', max_length=15)
    lastName = models.CharField(default='', max_length=15)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.CharField(default='', max_length=100)
    email_address = models.CharField(default='', max_length=40)


class Education(models.Model):
    institution = models.CharField(default='', max_length=50)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    grades = models.TextField(default='')


class Experience(models.Model):
    company = models.CharField(default='', max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    description = models.TextField(default='')


class Interests(models.Model):
    description = models.TextField(default='')