from django.db import models


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    dish_type = models.ForeignKey(
        "Topic",
        on_delete=models.CASCADE,
        related_name="newspapers",
    )
    publishers = models.ManyToManyField("Redactor", related_name="newspaper")

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

