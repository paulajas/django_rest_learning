# Generated by Django 4.0.4 on 2022-06-22 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0003_receipe_breakfastreceipe_dinnerreceipe_lunchreceipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meatreceipe',
            name='cookbook',
        ),
        migrations.AddField(
            model_name='receipe',
            name='cookbook',
            field=models.ManyToManyField(through='receipe.CookBookReceipe', to='receipe.cookbook'),
        ),
        migrations.AlterField(
            model_name='cookbookreceipe',
            name='receipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipe.receipe'),
        ),
    ]
