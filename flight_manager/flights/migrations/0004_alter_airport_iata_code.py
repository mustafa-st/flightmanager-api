# Generated by Django 4.1.5 on 2023-01-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0003_alter_flight_flight_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airport",
            name="iata_code",
            field=models.CharField(max_length=4, unique=True),
        ),
    ]