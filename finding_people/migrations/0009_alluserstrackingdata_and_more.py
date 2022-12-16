# Generated by Django 4.0.4 on 2022-12-11 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finding_people', '0008_trackinguserdata_uid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllUsersTrackingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True, unique=True)),
                ('from_database', models.CharField(max_length=50)),
                ('database_serial', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='trackinguserdata',
            name='tracking_progress',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='trackinguserdata',
            name='time_at_droped',
            field=models.TimeField(default=datetime.time(0, 31, 28, 988486)),
        ),
    ]