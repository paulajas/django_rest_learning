# Generated by Django 4.0.4 on 2022-06-22 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0001_initial'),
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
            name='receipe_ptr',
        ),
        migrations.RemoveField(
            model_name='lunchreceipe',
            name='receipe_ptr',
        ),
        migrations.RemoveField(
            model_name='meatreceipe',
            name='receipe_ptr',
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
            model_name='receipe',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='snackreceipe',
            name='receipe_ptr',
        ),
        migrations.RemoveField(
            model_name='vegereceipe',
            name='receipe_ptr',
        ),
        migrations.DeleteModel(
            name='BreakfastReceipe',
        ),
        migrations.DeleteModel(
            name='CookBookReceipe',
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
            name='Receipe',
        ),
        migrations.DeleteModel(
            name='SnackReceipe',
        ),
        migrations.DeleteModel(
            name='VegeReceipe',
        ),
    ]
