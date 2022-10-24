# Generated by Django 4.1.2 on 2022-10-23 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_review"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"default_permissions": ["view"], "get_latest_by": "created"},
        ),
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="products.product",
            ),
        ),
    ]
