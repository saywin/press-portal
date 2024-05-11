from django import forms
from django.contrib.auth.forms import UserCreationForm

from redact_radar.models import Redactor


class RedactorCreateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("first_name", "last_name", "years_of_experience", )