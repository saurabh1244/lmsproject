# Generated by Django 5.0 on 2024-06-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0012_alter_otptoken_otp_code_alter_product_frameworks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='fedcff', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='frameworks',
            field=models.CharField(choices=[('1', 'Django'), ('2', 'React'), ('3', 'Express'), ('4', 'Spring Boot'), ('5', 'Flask'), ('6', 'FastAPI'), ('7', 'Django REST framework'), ('8', 'Vue.js'), ('9', 'Angular'), ('10', 'Laravel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='programming_language',
            field=models.CharField(choices=[('1', 'Python'), ('2', 'JavaScript'), ('3', 'Java'), ('4', 'C#'), ('5', 'Ruby'), ('6', 'PHP'), ('7', 'Go'), ('8', 'Swift'), ('9', 'Kotlin'), ('10', 'TypeScript')], max_length=50),
        ),
    ]
