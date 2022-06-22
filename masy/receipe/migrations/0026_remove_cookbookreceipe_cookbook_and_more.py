# Generated by Django 4.0.4 on 2022-06-05 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0025_breakfastreceipe_dinnerreceipe_lunchreceipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookbookreceipe',
            name='cookbook',
        ),
        migrations.RemoveField(
            model_name='cookbookreceipe',
            name='receipe',
        ),
        migrations.RemoveField(
            model_name='dinnerreceipe',
            name='meatreceipe_ptr',
        ),
        migrations.RemoveField(
            model_name='lunchreceipe',
            name='meatreceipe_ptr',
        ),
        migrations.RemoveField(
            model_name='meatreceipe',
            name='receipe_ptr',
        ),
        migrations.RemoveField(
            model_name='meatreceipe',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='receipe',
            name='cookbook',
        ),
        migrations.RemoveField(
            model_name='receipe',
            name='country',
        ),
        migrations.RemoveField(
            model_name='receipe',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='receipe',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='snackreceipe',
            name='meatreceipe_ptr',
        ),
        migrations.DeleteModel(
            name='BreakfastReceipe',
        ),
        migrations.DeleteModel(
            name='CookBook',
        ),
        migrations.DeleteModel(
            name='CookBookReceipe',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='DinnerReceipe',
        ),
        migrations.DeleteModel(
            name='LunchReceipe',
        ),
        migrations.DeleteModel(
            name='MeatReceipe',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
        migrations.DeleteModel(
            name='SnackReceipe',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
