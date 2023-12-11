# Generated by Django 4.2.7 on 2023-11-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('emails', models.EmailField(max_length=120)),
                ('field_of_study', models.CharField(max_length=50)),
            ],
        ),
    ]
