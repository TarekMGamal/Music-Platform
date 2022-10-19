# Generated by Django 4.1.2 on 2022-10-19 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0002_album_isapproved"),
    ]

    operations = [
        migrations.RenameField(
            model_name="album", old_name="isApproved", new_name="is_approved",
        ),
        migrations.AlterField(
            model_name="album",
            name="creation_datetime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 10, 19, 15, 5, 34, 713976, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]