# Generated by Django 5.0.1 on 2024-02-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_remove_product_category_category_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="products",
        ),
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(default=1, upload_to="products"),
            preserve_default=False,
        ),
    ]
