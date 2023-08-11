# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.3 on 2023-08-12 04:26

import django.db.models.deletion
from django.db import migrations, models

import weblate.trans.mixins
import weblate.utils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0181_change_trans_chang_user_id_b1b554_idx"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Display name",
                        max_length=100,
                        verbose_name="Category name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Name used in URLs and filenames.",
                        max_length=100,
                        validators=[weblate.utils.validators.validate_slug],
                        verbose_name="URL slug",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_set",
                        to="trans.category",
                        verbose_name="Category",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            bases=(
                models.Model,
                weblate.trans.mixins.PathMixin,
                weblate.trans.mixins.CacheKeyMixin,
            ),
        ),
        migrations.AddField(
            model_name="component",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trans.category",
                verbose_name="Category",
            ),
        ),
    ]
