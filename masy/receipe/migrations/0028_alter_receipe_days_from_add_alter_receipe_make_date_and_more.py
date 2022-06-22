# Generated by Django 4.0.4 on 2022-06-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0027_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='days_from_add',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='make_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_country_id', to='receipe.tagcountry'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='text_receipe',
            field=models.TextField(),
        ),
    ]