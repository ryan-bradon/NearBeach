# Generated by Django 5.0.1 on 2024-03-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NearBeach", "0029_alter_sprint_sprint_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sprint",
            name="sprint_end_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="sprint",
            name="sprint_start_date",
            field=models.DateTimeField(),
        ),
    ]
