# Generated by Django 3.0.7 on 2020-06-24 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_auto_20200622_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_table',
            old_name='bankcharges',
            new_name='bksc',
        ),
    ]
