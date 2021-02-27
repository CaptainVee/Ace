from django import forms
from .models import Announcement
# class AnnouncementUpdateForm(forms.Form):
#     announced = forms.BooleanField(required=False)

class AnnouncementUpdateForm(forms.Form):
	approve_all = forms.BooleanField(required=False)

class ContributorForm(forms.Form):
	email = forms.EmailField(max_length=150)