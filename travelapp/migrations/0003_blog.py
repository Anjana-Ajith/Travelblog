# Generated by Django 3.2.7 on 2021-11-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='picture')),
                ('date', models.IntegerField()),
                ('day', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]