# Generated by Django 4.0.4 on 2023-01-14 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_cookbook_receipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='text',
            new_name='text_receipe',
        ),
    ]