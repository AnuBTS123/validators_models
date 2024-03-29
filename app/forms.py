from django import forms
from app.models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput())

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot is catched')