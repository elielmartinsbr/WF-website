# Generated by Django 3.2.12 on 2022-03-21 08:46

import django.db.models.deletion
import timezone_field.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("teaser", models.TextField(blank=True, max_length=100, null=True)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("rich_text", wagtail.blocks.RichTextBlock()),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "width",
                                            wagtail.blocks.IntegerBlock(
                                                help_text="Enter the desired image width value in pixels up to 800 max.",
                                                max_value=800,
                                                min_value=0,
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField(blank=True, null=True)),
                (
                    "timezone",
                    timezone_field.fields.TimeZoneField(
                        choices_display="WITH_GMT_OFFSET",
                        default="US/Pacific",
                    ),
                ),
                ("website", models.URLField(blank=True, max_length=300, null=True)),
                ("drupal_node_id", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "events",
                "ordering": ["start_date"],
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="EventsIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
