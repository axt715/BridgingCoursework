from django import forms
from cv.models import *


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ('firstName', 'lastName','date_of_birth', 'address', 'email_address')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institution', 'start_date', 'end_date', 'grades')


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'start_date', 'end_date', 'description')


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = ('description',)