from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from redact_radar.models import Redactor, Newspaper


class CustomCheckboxField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.CheckboxSelectMultiple()


class RedactorCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "email",
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("first_name", "last_name", "years_of_experience",)


class NewspaperCreateForm(forms.ModelForm):
    dish_type = CustomCheckboxField(
        queryset=get_user_model().objects.all(),
        required=False
    )
    publishers = CustomCheckboxField(
        queryset=get_user_model().objects.all(),
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"
