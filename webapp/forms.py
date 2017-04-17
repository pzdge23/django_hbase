from django import forms
from .choices import *
# class SubmitUrlForm(forms.Form):
#     years = [str(i) for i in range(2000, 2020)]
#     url = forms.CharField(label="Submit url")

class IndexForm(forms.Form):
    year = forms.ChoiceField(choices = YEARS, label="year choices ", initial="", widget=forms.Select(), required=True)

class YearForm(forms.Form):
    # year = forms.CharField(initial = ,disabled=True)
    month = forms.ChoiceField(choices = MONTHS, label="month choices ", initial = "", widget = forms.Select(), required=True)

class MonthForm(forms.Form):
    # year = forms.CharField(disabled=True)
    # month = forms.CharField(disabled=True)
    day = forms.ChoiceField(choices = DATES, label="date choices ", initial = "", widget = forms.Select(), required = True)
