# Generated by Django 4.0.6 on 2022-08-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('course_number', models.IntegerField()),
                ('professor_name', models.CharField(max_length=150)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('group', models.IntegerField()),
                ('day_1', models.IntegerField(choices=[(0, 'Saturday'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday')], max_length=1)),
                ('day_2', models.IntegerField(choices=[(0, 'Saturday'), (1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday')], max_length=1)),
            ],
        ),
    ]