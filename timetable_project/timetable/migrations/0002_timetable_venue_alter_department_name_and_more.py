# Generated by Django 5.1.4 on 2024-12-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='venue',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lecturer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]