from django import forms
from .models import Announcement
# class AnnouncementUpdateForm(forms.Form):
#     announced = forms.BooleanField(required=False)

class ApproveForm(forms.Form):
	approve_all = forms.BooleanField(required=False)

class AnnouncementUpdateForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = ['title', 'content', 'image']

class ContributorForm(forms.Form):
	email = forms.EmailField(max_length=150)