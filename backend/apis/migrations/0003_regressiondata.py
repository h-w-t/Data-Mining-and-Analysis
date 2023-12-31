# Generated by Django 4.2.2 on 2023-06-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0002_aprioridb"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegressionData",
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
                ("x", models.FloatField()),
                ("y", models.FloatField()),
            ],
            options={
                "verbose_name": "回归数据",
                "db_table": "RegressionData",
            },
        ),
    ]
