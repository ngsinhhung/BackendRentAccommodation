# Generated by Django 5.0 on 2023-12-28 04:08

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentApp', '0003_delete_role_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar_user',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Quản trị viên'), ('HOST', 'Chủ nhà'), ('TENANT', 'Người thuê')], default='TENANT', max_length=6),
        ),
    ]
