# Generated by Django 3.0.7 on 2020-06-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_user_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_registration',
        ),
    ]