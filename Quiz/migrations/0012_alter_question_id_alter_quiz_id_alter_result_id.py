# Generated by Django 4.1.2 on 2022-10-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Quiz", "0011_remove_quiz_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]