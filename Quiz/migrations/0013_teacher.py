# Generated by Django 4.1.2 on 2022-10-06 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Quiz", "0012_alter_question_id_alter_quiz_id_alter_result_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                # (
                #     "id",
                #     models.BigAutoField(
                #         auto_created=True,
                #         primary_key=True,
                #         serialize=False,
                #         verbose_name="ID",
                #     ),
                # ),
                ("email", models.EmailField(max_length=254, verbose_name="")),
                ("first_name", models.CharField(default="", max_length=20)),
                ("last_name", models.CharField(default="", max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
