from django import forms

from redact_radar.models import Redactor


class RedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = "__all__"
