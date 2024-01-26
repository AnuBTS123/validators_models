from django.db import models
from django.core import validators
from django import forms
# Create your models here.

def validate_for_c(data):
    if data.lower().startswith('c'):
        raise forms.ValidationError('started with c')

class Student(models.Model):
    Sname=models.CharField(max_length=100,validators=[validate_for_c])
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.Sname
    