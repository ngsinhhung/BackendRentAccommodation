# Generated by Django 5.0 on 2023-12-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentApp', '0002_remove_user_follower_remove_user_following_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Quan Tri Vien'), ('HOST', 'Chu Nha'), ('TENANT', 'Nguoi Thue Tro')], default='TENANT', max_length=6),
        ),
    ]