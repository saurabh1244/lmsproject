# Generated by Django 5.0 on 2024-06-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0009_product_frameworks_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='programming_language',
            field=models.CharField(choices=[(1, 'Python'), (2, 'JavaScript'), (3, 'Java'), (4, 'C++'), (5, 'Sql'), (6, 'C'), (7, 'Rust'), (8, 'Swipt'), (9, 'Kotlin'), (10, 'nosql')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='e1c4ae', max_length=6),
        ),
    ]
