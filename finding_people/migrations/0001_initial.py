# Generated by Django 4.0.4 on 2022-12-10 16:20

from django.db import migrations, models
import finding_people.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AadharData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(unique=True)),
                ('VID', models.IntegerField(unique=True)),
                ('profile', models.ImageField(upload_to=finding_people.models.PathAndRename('Aadhar Data'))),
                ('name', models.CharField(max_length=50)),
                ('DOB', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CascadeAndTrainerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file_name', models.FileField(upload_to='CascadeAndTrainer')),
            ],
        ),
        migrations.CreateModel(
            name='FIRData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fir_id', models.IntegerField(unique=True)),
                ('profile', models.ImageField(upload_to=finding_people.models.PathAndRename('FIR Data'))),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('fir_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LoggedInData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, max_length=50, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingUserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('profile', models.ImageField(blank=True, upload_to=finding_people.models.PathAndRename('TrackingImage'))),
            ],
        ),
        migrations.CreateModel(
            name='TrainedDataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('aadhar_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainigImagesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('from_database', models.CharField(default='None', max_length=50)),
                ('image', models.ImageField(blank=True, upload_to=finding_people.models.PathAndRename('TrainigImage'))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
