# Generated by Django 4.1 on 2022-08-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
