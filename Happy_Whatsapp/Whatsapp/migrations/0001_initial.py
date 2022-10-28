# Generated by Django 4.1.2 on 2022-10-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Login",
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
                ("user_name", models.CharField(max_length=50)),
                ("user_email", models.CharField(max_length=100)),
                ("user_password", models.CharField(max_length=20)),
            ],
        ),
    ]
