# Generated by Django 4.0.4 on 2022-05-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0015_rename_to_cookbook_cookbookreceipe_cookbook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='to_country',
            new_name='country',
        ),
    ]
