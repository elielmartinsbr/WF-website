# Generated by Django 3.2.13 on 2022-05-11 10:31

import re

import django.core.validators
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations

import documents.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("wf_pages", "0002_alter_wfpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wfpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("document", documents.blocks.DocumentEmbedBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(
                            features=[
                                "h2",
                                "h3",
                                "h4",
                                "bold",
                                "italic",
                                "ol",
                                "ul",
                                "hr",
                                "link",
                                "document-link",
                                "image",
                                "superscript",
                                "superscript",
                                "strikethrough",
                                "blockquote",
                            ],
                        ),
                    ),
                    ("quote", wagtail.blocks.BlockQuoteBlock()),
                    (
                        "target",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "target_slug",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used to link to a specific location within this page. Slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                        validators=(
                                            django.core.validators.RegexValidator(
                                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                "invalid",
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),
    ]
