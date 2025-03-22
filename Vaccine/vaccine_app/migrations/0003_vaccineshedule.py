# Generated by Django 5.1.6 on 2025-02-20 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vaccine_app", "0002_complaints"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vaccineshedule",
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
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "hospital_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vaccine_app.hospital",
                    ),
                ),
                (
                    "vaccine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="vaccine_app.vaccine",
                    ),
                ),
            ],
        ),
    ]
