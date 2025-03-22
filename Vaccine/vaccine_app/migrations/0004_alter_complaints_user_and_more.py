# Generated by Django 5.1.6 on 2025-02-20 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vaccine_app", "0003_vaccineshedule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaints",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="vaccineshedule",
            name="hospital_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="vaccine_app.hospital",
            ),
        ),
        migrations.AlterField(
            model_name="vaccineshedule",
            name="vaccine",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="vaccine_app.vaccine",
            ),
        ),
    ]
