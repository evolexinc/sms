# Generated by Django 4.2.14 on 2024-09-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('class_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('class_seats', models.IntegerField()),
                ('class_location', models.CharField(max_length=50)),
                ('class_subjects', models.CharField(max_length=50)),
                ('class_teacher', models.CharField(max_length=50)),
            ],
        ),
    ]
