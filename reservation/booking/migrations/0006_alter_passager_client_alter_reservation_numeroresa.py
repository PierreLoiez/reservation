# Generated by Django 4.2 on 2024-04-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0005_passager_client_alter_reservation_numeroresa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passager",
            name="client",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="booking.client",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="numeroResa",
            field=models.IntegerField(
                default=81806068, primary_key=True, serialize=False
            ),
        ),
    ]