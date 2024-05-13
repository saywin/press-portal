from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from redact_radar.forms import NewspaperSearchForm
from redact_radar.models import Topic, Newspaper
from redact_radar.views import (
    NewspaperListView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
)

NEWSPAPER_URL = reverse("redact_radar:newspaper-list")


class PublicNewspaperTests(TestCase):
    def test_newspaper_create_update_delete_login_required(self):
        newspaper_create = self.client.get(
            reverse("redact_radar:newspaper-create")
        )
        newspaper_update = self.client.get(
            reverse("redact_radar:newspaper-update", args=[1])
        )
        newspaper_delete = self.client.get(
            reverse("redact_radar:newspaper-delete", args=[1])
        )
        self.assertEqual(newspaper_create.status_code, 302)
        self.assertEqual(newspaper_update.status_code, 302)
        self.assertEqual(newspaper_delete.status_code, 302)


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="test123",
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="test-topic")
        self.newspaper = Newspaper.objects.create(
            title="test-newspaper",
            content="test-content"
        )
        self.response = self.client.get(NEWSPAPER_URL)

    def test_newspaper_create_login_required(self):
        newspaper_create = self.client.get(
            reverse("redact_radar:newspaper-create")
        )
        self.assertEqual(newspaper_create.status_code, 200)

    def test_newspaper_update_login_required(self):
        newspaper_update = self.client.get(
            reverse("redact_radar:newspaper-update", args=[self.newspaper.id])
        )
        self.assertEqual(newspaper_update.status_code, 200)

    def test_newspaper_delete_login_required(self):
        newspaper_delete = self.client.get(reverse(
            "redact_radar:newspaper-delete", args=[self.newspaper.id])
        )
        self.assertEqual(newspaper_delete.status_code, 200)

    def test_newspaper_paginate(self):
        self.assertEqual(NewspaperListView.paginate_by, 3)

    def test_topic_context(self):
        newspaper = Newspaper.objects.all()
        self.assertEqual(
            list(self.response.context["newspaper_list"]),
            list(newspaper)
        )

    def test_newspaper_template_used(self):
        self.assertTemplateUsed(
            self.response, "redact_radar/newspaper_list.html"
        )

    def test_newspaper_context_data(self):
        form = self.response.context["search_form"]
        self.assertIsInstance(form, NewspaperSearchForm)
        self.assertEqual(form.initial["title"], "")

    def test_newspaper_create_success_url(self):
        view = NewspaperCreateView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)

    def test_car_update_success_url(self):
        view = NewspaperUpdateView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)

    def test_car_delete_success_url(self):
        view = NewspaperDeleteView()
        view.object = self.newspaper
        self.assertEqual(view.get_success_url(), NEWSPAPER_URL)
