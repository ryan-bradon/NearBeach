# Generated by Django 5.0.7 on 2024-09-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NearBeach", "0032_rename_kanban_comment_permissionset_kanban_note_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="permissionset",
            name="organisation_note",
            field=models.IntegerField(
                choices=[(0, "No Permission"), (1, "Has Permission")], default=0
            ),
        ),
    ]