# Generated by Django 3.0.5 on 2022-10-06 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_auto_20221006_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
