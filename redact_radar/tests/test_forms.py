from django.contrib.auth import get_user_model
from django.test import TestCase

from redact_radar.forms import RedactorCreateForm, RedactorUpdateForm, NewspaperSearchForm, NewspaperUpdateForm, \
    NewspaperCreateForm
from redact_radar.models import Newspaper, Topic


class RedactorFormTests(TestCase):
    def setUp(self):
        self.form_data = {
            "username": "new_user",
            "password1": "user55test",
            "password2": "user55test",
            "years_of_experience": 3,
            "first_name": "First user",
            "last_name": "Last user",
            "email": "user@localhost.com"
        }
        self.form = RedactorCreateForm(data=self.form_data)

    def test_redactor_creation_form_is_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_redactor_creation_form_invalid_data(self):
        self.form.is_valid()
        self.assertTrue(self.form.cleaned_data, self.form_data)

    def test_redactor_update_form_fields(self):
        form = RedactorUpdateForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('years_of_experience', form.fields)

    def test_redactor_update_form_validation(self):
        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'years_of_experience': 7
        }
        form = RedactorUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['first_name'], 'Test')
        self.assertEqual(form.cleaned_data['last_name'], 'User')
        self.assertEqual(form.cleaned_data['years_of_experience'], 7)


class NewspaperFormTests(TestCase):
    def setUp(self):
        self.topic1 = Topic.objects.create(name="Politics")
        self.topic2 = Topic.objects.create(name="Sports")
        self.user1 = get_user_model().objects.create(
            username="user1",
            password="1qazcde3"
        )
        self.user2 = get_user_model().objects.create(
            username="user2",
            password="1qazcde3"
        )

    def test_newspaper_create_form(self):
        form_data = {
            "title": "Newspaper Title",
            "content": "Newspaper-content",
            "dish_type": [self.topic1.pk, self.topic2.pk],
            "publishers": [self.user1.pk, self.user2.pk]
        }
        form = NewspaperCreateForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_newspaper_update_form(self):
        newspaper = Newspaper.objects.create(title="Existing Title")
        form_data = {
            "title": "Updated Title",
            "content": "Updated-content",
            "dish_type": [self.topic1.pk],
            "publishers": [self.user1.pk]
        }
        form = NewspaperUpdateForm(data=form_data, instance=newspaper)
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form_data = {
            "title": "Search Query"
        }
        form = NewspaperSearchForm(data=form_data)
        self.assertTrue(form.is_valid())