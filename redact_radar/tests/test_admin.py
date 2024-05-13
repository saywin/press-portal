from django.contrib.admin import site

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from redact_radar.models import Newspaper


class RedactorAdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="1qazcde3"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="testredactor",
            years_of_experience=4,
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:redact_radar_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience(self):
        url = reverse(
            "admin:redact_radar_redactor_change",
            args=[self.redactor.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_add_detail_years_of_experience(self):
        url = reverse("admin:redact_radar_redactor_add")
        res = self.client.get(url)
        self.assertContains(res, "years_of_experience")


class NewspaperAdminSiteTests(TestCase):
    def test_admin_list_display(self):
        self.assertIn("title", site._registry[Newspaper].list_display)
        self.assertIn("get_topics", site._registry[Newspaper].list_display)
        self.assertIn("published_date", site._registry[Newspaper].list_display)

    def test_admin_search_fields(self):
        self.assertIn("title", site._registry[Newspaper].search_fields)

    def test_admin_ordering(self):
        self.assertEqual(site._registry[Newspaper].ordering, ("-published_date",))
