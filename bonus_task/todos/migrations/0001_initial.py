# Generated by Django 5.0.2 on 2024-03-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=1000)),
                ("due_date", models.DateTimeField(null=True)),
                ("status", models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
