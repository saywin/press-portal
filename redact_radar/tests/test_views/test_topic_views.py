from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from redact_radar.models import Topic
from redact_radar.views import (
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
)

TOPIC_URL = reverse("redact_radar:topic-list")


class PublicTopicViewTests(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertEqual(res.status_code, 302)


class PrivateTopicViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="test123",
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="sport")
        self.response = self.client.get(TOPIC_URL)

    def test_login_required(self):
        self.assertEqual(self.response.status_code, 200)

    def test_topic_template_used(self):
        self.assertTemplateUsed(self.response, "redact_radar/topic_list.html")

    def test_topic_context(self):
        topics = Topic.objects.all()
        self.assertEqual(
            list(self.response.context["topic_list"]),
            list(topics)
        )

    def test_topic_paginate(self):
        self.assertEqual(TopicListView.paginate_by, 4)

    def test_topic_create_success_url(self):
        view = TopicCreateView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)

    def test_topic_update_success_url(self):
        view = TopicUpdateView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)

    def test_topic_delete_success_url(self):
        view = TopicDeleteView()
        view.object = self.topic
        self.assertEqual(view.get_success_url(), TOPIC_URL)
