from django import forms
from django.contrib.auth import models
from django.forms import fields
from .models import Interview

class InterviewForm(forms.ModelForm):
	class Meta:
		model = Interview
		fields = ['vid1', 'vid2', 'vid3']