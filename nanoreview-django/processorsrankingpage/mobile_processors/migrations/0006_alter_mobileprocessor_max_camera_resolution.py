# Generated by Django 5.1.1 on 2024-11-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_processors', '0005_alter_mobileprocessor_l2_cache_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileprocessor',
            name='max_camera_resolution',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
