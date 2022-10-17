# Generated by Django 4.1.2 on 2022-10-17 11:27

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0003_rename_zip_code_address_postal_code_address_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="country",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="customer",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                editable=False,
                populate_from="get_full_name",
                unique=True,
            ),
        ),
    ]
