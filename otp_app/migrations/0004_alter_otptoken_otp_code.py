# Generated by Django 5.0 on 2024-06-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0003_rename_otp_expired_at_otptoken_otp_expires_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='8baaf7', max_length=6),
        ),
    ]
