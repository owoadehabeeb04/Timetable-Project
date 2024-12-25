# Generated by Django 5.1.4 on 2024-12-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_timetable_venue_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='course',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lecturer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='time',
            field=models.TimeField(),
        ),
    ]
