# Generated by Django 5.0 on 2024-01-04 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentApp', '0005_alter_follow_follower_alter_follow_following_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='parent_comment',
        ),
    ]