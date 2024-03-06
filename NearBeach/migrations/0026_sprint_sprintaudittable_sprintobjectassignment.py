# Generated by Django 5.0.1 on 2024-03-06 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "NearBeach",
            "0025_rename_project_status_order_listofprojectstatus_project_status_sort_order_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sprint",
            fields=[
                ("sprint_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "sprint_name",
                    models.CharField(default="empty sprint", max_length=100),
                ),
                ("total_story_points", models.IntegerField(default=0)),
                ("completed_story_points", models.IntegerField(default=0)),
                (
                    "sprint_status",
                    models.CharField(
                        blank=True,
                        choices=[("Current", "Current"), ("Finished", "Finished")],
                        default="Current",
                        max_length=10,
                    ),
                ),
                ("sprint_start_date", models.DateTimeField(auto_now_add=True)),
                ("sprint_end_date", models.DateTimeField(auto_now_add=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "change_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_change_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.project",
                    ),
                ),
                (
                    "requirement",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.requirement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SprintAuditTable",
            fields=[
                (
                    "sprint_audit_table_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("story_point_cost", models.IntegerField(default=0)),
                (
                    "higher_order_status",
                    models.CharField(
                        choices=[
                            ("Backlog", "Backlog"),
                            ("Normal", "Normal"),
                            ("Blocked", "Blocked"),
                            ("Closed", "Closed"),
                        ],
                        default="Normal",
                        max_length=10,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "change_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_change_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.project",
                    ),
                ),
                (
                    "requirement_item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.requirementitem",
                    ),
                ),
                (
                    "sprint_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.sprint",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SprintObjectAssignment",
            fields=[
                (
                    "sprint_object_assignment_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "change_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_change_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.project",
                    ),
                ),
                (
                    "requirement_item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.requirementitem",
                    ),
                ),
                (
                    "sprint_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.sprint",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NearBeach.task",
                    ),
                ),
            ],
        ),
    ]
