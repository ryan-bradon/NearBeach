# Generated by Django 5.0.7 on 2024-07-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NearBeach", "0029_alter_userjob_job_date_objecttemplate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduledobject",
            name="schedule_object_title",
            field=models.CharField(default="Scheduled Object", max_length=255),
            preserve_default=False,
        ),
    ]
