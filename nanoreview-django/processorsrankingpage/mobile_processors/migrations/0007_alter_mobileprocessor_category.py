# Generated by Django 5.1.1 on 2024-11-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_processors', '0006_alter_mobileprocessor_max_camera_resolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileprocessor',
            name='category',
            field=models.CharField(choices=[('FLAGSHIP', 'Flagship'), ('MID_RANGE', 'Mid Range'), ('LOW_END', 'Low end')], max_length=20, null=True),
        ),
    ]
