# Generated by Django 4.1.2 on 2022-10-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Quiz", "0019_alter_teacher_first_name_alter_teacher_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="instructions",
            field=models.CharField(default="", max_length=600),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="quiz_name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
