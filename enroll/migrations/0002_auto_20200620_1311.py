# Generated by Django 3.0.7 on 2020-06-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='bank',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='bankcharges',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='brand',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='cheque',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='cltnamt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='cltndate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='collectedby',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='customercode',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='doptdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='duedate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invamt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='invdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='paymentmode',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='Pending', max_length=70),
        ),
        migrations.AddField(
            model_name='user',
            name='utrno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]