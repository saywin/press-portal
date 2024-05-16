from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from press_portal import settings


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )
    dish_type = models.ManyToManyField(
        "Topic",
        related_name="newspapers",
    )

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return f"title: {self.title}, topic: {self.dish_type}"


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(50)],
        default=0
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
