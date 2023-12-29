# Generated by Django 4.1.1 on 2023-04-17 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("NearBeach", "0021_project_status_task_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="project_status",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="status",
            new_name="project_status",
        ),
        migrations.RemoveField(
            model_name="task",
            name="task_status",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="status",
            new_name="task_status",
        ),
        migrations.RemoveField(
            model_name="listofrequirementitemstatus",
            name="status_is_closed",
        ),
        migrations.RemoveField(
            model_name="listofrequirementstatus",
            name="requirement_status_is_closed",
        ),
    ]