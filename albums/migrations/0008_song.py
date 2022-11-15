# Generated by Django 4.1.2 on 2022-10-25 15:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0007_remove_album_creation_datetime"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("name", models.CharField(default=None, max_length=100)),
                ("image", models.ImageField(upload_to="image/")),
                (
                    "audio",
                    models.FileField(
                        upload_to="audio/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["mp3", "wav"]
                            )
                        ],
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="albums.album"
                    ),
                ),
            ],
        ),
    ]