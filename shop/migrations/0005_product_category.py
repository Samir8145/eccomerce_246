# Generated by Django 5.0.1 on 2024-02-06 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_remove_category_products_category_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
            ),
            preserve_default=False,
        ),
    ]
