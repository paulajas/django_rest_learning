# Generated by Django 4.0.4 on 2022-05-27 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0011_countryreceipe_country_to_receipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='to_receipe',
        ),
        migrations.DeleteModel(
            name='CountryReceipe',
        ),
    ]
