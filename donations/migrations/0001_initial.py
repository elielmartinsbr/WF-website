# Generated by Django 3.2.12 on 2022-03-21 08:46

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="DonatePage",
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
                (
                    "suggested_donation_amounts",
                    wagtail.fields.StreamField(
                        [
                            (
                                "suggested_donation_amounts",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "once",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.IntegerBlock(
                                                    label="Amount",
                                                ),
                                            ),
                                        ),
                                        (
                                            "monthly",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.IntegerBlock(
                                                    label="Amount",
                                                ),
                                            ),
                                        ),
                                        (
                                            "yearly",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.IntegerBlock(
                                                    label="Amount",
                                                ),
                                            ),
                                        ),
                                    ],
                                    max_num=1,
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="DonorAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "street_address",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "extended_address",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "po_box_number",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="P.O. Box, if relevant",
                        max_length=32,
                    ),
                ),
                (
                    "locality",
                    models.CharField(
                        blank=True,
                        help_text="Locality or city",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="State or region",
                        max_length=255,
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        help_text="Postal code (or zipcode)",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        default="United States",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        choices=[("mailing", "Mailing"), ("worship", "Worship")],
                        max_length=255,
                    ),
                ),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Donation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField()),
                (
                    "recurrence",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("once", "Once"),
                            ("monthly", "Monthly"),
                            ("yearly", "Yearly"),
                        ],
                        default="once",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("donor_given_name", models.CharField(max_length=255)),
                ("donor_family_name", models.CharField(max_length=255)),
                (
                    "donor_organization",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "donor_email",
                    models.EmailField(
                        help_text="Please enter your email",
                        max_length=254,
                    ),
                ),
                ("paid", models.BooleanField(default=False)),
                (
                    "braintree_transaction_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "braintree_subscription_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "donor_address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="donations.donoraddress",
                    ),
                ),
            ],
        ),
    ]
