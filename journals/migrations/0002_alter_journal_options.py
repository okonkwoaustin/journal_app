# Generated by Django 5.2.4 on 2025-07-25 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("journals", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="journal",
            options={"ordering": ["-date_created"]},
        ),
    ]
