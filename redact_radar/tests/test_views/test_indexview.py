from django.test import TestCase
from django.urls import reverse

from redact_radar.models import Newspaper, Topic, Redactor


class IndexViewTest(TestCase):
    def setUp(self):
        Topic.objects.create(name="Topic 1")
        Topic.objects.create(name="Topic 2")
        Redactor.objects.create(
            username="redactor1",
            password="2wsxcvfr4",
        )
        Newspaper.objects.create(
            title="Newspaper 1",
            content="Newspaper",
        )
        Newspaper.objects.create(
            title="Newspaper 2",
            content="Newspaper2"
        )

    def test_index_view_context(self):
        response = self.client.get(reverse('redact_radar:index'))
        print(response.context)
        print(response.context.keys())
        self.assertEqual(response.context.get('num_newspapers'), 2)
        self.assertEqual(response.context['num_topics'], 2)
        self.assertEqual(response.context['num_redactors'], 1)
