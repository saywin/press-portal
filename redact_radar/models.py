from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from press_portal import settings


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    dish_type = models.ManyToManyField(
        "Topic",
        related_name="newspapers",
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspaper"
    )

    class Meta:
        ordering = ("title", )

    def __str__(self):
        return f"title: {self.title}, topic: {self.dish_type}"


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
