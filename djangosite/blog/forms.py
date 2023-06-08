from django import forms
from .models import *

class CreateNewNews(forms.ModelForm):
	class Meta:
		model = news
		fields = ["title","tag","text"]
		