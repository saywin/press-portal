from django.core.exceptions import ValidationError
from django.test import TestCase

from redact_radar.models import Topic, Redactor, Newspaper


class TopicModelTest(TestCase):

    def test_topic_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic),
                         topic.name)


class RedactModelTest(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            username="test",
            password="1qazcde3",
            years_of_experience=3
        )

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.first_name} "
            f"{self.redactor.last_name} "
            f"({self.redactor.username})"
        )

    def test_years_of_experience_min_value(self):
        with self.assertRaises(ValidationError):
            redactor = Redactor.objects.create(
                username="test_2",
                password="1qazcde3",
                years_of_experience=-1,
            )
            redactor.full_clean()

    def test_years_of_experience_max_value(self):
        with self.assertRaises(ValidationError):
            redactor = Redactor.objects.create(
                username="test_2",
                password="1qazcde3",
                years_of_experience=51,
            )
            redactor.full_clean()

    def test_crete_with_years_of_experience(self):
        self.assertEqual(self.redactor.years_of_experience, 3)


class NewspaperModelTest(TestCase):
    def test_newspaper_str(self):
        newspaper = Newspaper.objects.create(
            title="test",
            content="test_content"
        )
        self.assertEqual(
            str(newspaper),
            f"title: {newspaper.title}, topic: {newspaper.dish_type}"
        )
