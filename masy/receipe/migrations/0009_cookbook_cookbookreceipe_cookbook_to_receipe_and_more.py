# Generated by Django 4.0.4 on 2022-05-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0008_picture_picturereceipe_picture_to_receipe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CookBookReceipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.IntegerField(choices=[(1, 'Bad'), (2, 'Lower Medium'), (3, 'Medium'), (4, 'Lower Good'), (5, 'Good'), (6, 'Excelent')])),
                ('to_cookbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipe.cookbook')),
                ('to_receipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receipe.receipe')),
            ],
        ),
        migrations.AddField(
            model_name='cookbook',
            name='to_receipe',
            field=models.ManyToManyField(through='receipe.CookBookReceipe', to='receipe.receipe'),
        ),
        migrations.AddField(
            model_name='receipe',
            name='to_cookbook',
            field=models.ManyToManyField(through='receipe.CookBookReceipe', to='receipe.cookbook'),
        ),
    ]