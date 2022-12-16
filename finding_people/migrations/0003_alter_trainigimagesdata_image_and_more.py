# Generated by Django 4.0.4 on 2022-12-11 11:42

from django.db import migrations, models
import finding_people.models


class Migration(migrations.Migration):

    dependencies = [
        ('finding_people', '0002_aadhardata_serial_firdata_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainigimagesdata',
            name='image',
            field=models.ImageField(blank=True, upload_to=finding_people.models.PathAndRename('TrainingImage')),
        ),
        migrations.AlterField(
            model_name='trainigimagesdata',
            name='serial',
            field=models.IntegerField(unique=True),
        ),
    ]