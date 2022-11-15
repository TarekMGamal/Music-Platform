# Generated by Django 4.1.2 on 2022-10-19 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0003_rename_isapproved_album_is_approved_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="creation_datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
    ]