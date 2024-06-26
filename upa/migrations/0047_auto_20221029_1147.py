# Generated by Django 3.2.5 on 2022-10-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upa', '0046_alter_personalinformation_customer_nature'),
    ]

    operations = [
        migrations.AddField(
            model_name='upaaddress',
            name='active_mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='upaaddress',
            name='customer_language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Hindi', 'Hindi')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='upaaddress',
            name='delivery_location',
            field=models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Present', 'Present')], max_length=40, null=True),
        ),
    ]
