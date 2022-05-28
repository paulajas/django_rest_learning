# Generated by Django 4.0.4 on 2022-05-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0014_rename_to_picture_receipe_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookbookreceipe',
            old_name='to_cookbook',
            new_name='cookbook',
        ),
        migrations.RenameField(
            model_name='cookbookreceipe',
            old_name='to_receipe',
            new_name='receipe',
        ),
        migrations.RemoveField(
            model_name='receipe',
            name='to_cookbook',
        ),
        migrations.AddField(
            model_name='cookbook',
            name='receipe',
            field=models.ManyToManyField(through='receipe.CookBookReceipe', to='receipe.receipe'),
        ),
    ]
