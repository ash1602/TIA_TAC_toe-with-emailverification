# Generated by Django 4.0.1 on 2022-01-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100, unique=True)),
                ('connected_users', models.IntegerField()),
            ],
        ),
    ]
