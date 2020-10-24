from django import forms
from .models import City

class HtmlForm(forms.Form):
	name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):

	class Meta(object):
		model = City
		fields = ('name', )