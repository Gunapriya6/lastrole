# Generated by Django 3.0 on 2021-05-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='proof_type',
            field=models.CharField(choices=[('P', 'Passbook'), ('A', 'adhar')], default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
    ]