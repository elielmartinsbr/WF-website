# Generated by Django 4.1.6 on 2023-02-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0005_meeting_meeting_drupal__cf6e0d_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="meeting",
            index=models.Index(
                fields=["civicrm_id"],
                name="meeting_civicrm_c09b04_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="organization",
            index=models.Index(
                fields=["civicrm_id"],
                name="organizatio_civicrm_4d8d5d_idx",
            ),
        ),
    ]
