from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from redact_radar.models import Redactor
from redact_radar.views import (
    RedactorListView,
    RedactorCreateView,
    RedactorUpdateView
)

REDACTOR_URL = reverse("redact_radar:redactor-list")


class PublicRedactorViewTests(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertEqual(res.status_code, 302)


class PrivateRedactorViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test123",
        )
        self.client.force_login(self.user)
        self.response = self.client.get(REDACTOR_URL)

    def test_login_required(self):
        self.assertEqual(self.response.status_code, 200)

    def test_redactor_template_used(self):
        self.assertTemplateUsed(
            self.response,
            "redact_radar/redactor_list.html"
        )

    def test_redactor_context(self):
        redactor = Redactor.objects.all()
        self.assertEqual(
            list(self.response.context["redactor_list"]),
            list(redactor)
        )

    def test_redactor_paginate(self):
        self.assertEqual(RedactorListView.paginate_by, 3)

    def test_redactor_create_success_url(self):
        view = RedactorCreateView()
        view.object = self.user
        self.assertEqual(view.get_success_url(), REDACTOR_URL)

    def test_topic_update_success_url(self):
        view = RedactorUpdateView()
        view.object = self.user
        self.assertEqual(view.get_success_url(), REDACTOR_URL)

    def test_create_author(self):
        form_data = {
            "username": "new_user",
            "password1": "user55test",
            "password2": "user55test",
            "years_of_experience": 3,
            "first_name": "First user",
            "last_name": "Last user",
        }
        self.client.post(
            reverse("redact_radar:redactor-create"),
            data=form_data,
        )
        new_user = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"],
        )
