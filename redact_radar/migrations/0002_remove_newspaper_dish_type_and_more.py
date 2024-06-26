# Generated by Django 5.0.4 on 2024-05-07 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("redact_radar", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newspaper",
            name="dish_type",
        ),
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AddField(
            model_name="newspaper",
            name="dish_type",
            field=models.ManyToManyField(
                related_name="newspapers", to="redact_radar.topic"
            ),
        ),
    ]
