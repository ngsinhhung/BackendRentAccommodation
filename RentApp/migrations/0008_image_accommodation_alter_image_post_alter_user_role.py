# Generated by Django 5.0 on 2024-01-08 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentApp', '0007_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='accommodation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accommodation', to='RentApp.accommodation'),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='RentApp.post'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('TENANT', 'Người thuê'), ('ADMIN', 'Quản trị viên'), ('HOST', 'Chủ nhà')], default='TENANT', max_length=6),
        ),
    ]
