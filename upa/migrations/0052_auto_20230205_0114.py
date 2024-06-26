# Generated by Django 3.2.5 on 2023-02-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upa', '0051_auto_20230126_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiarydetails',
            name='relation_upa',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Daughter', 'Daughter'), ('Son', 'Son'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='update_age_dob',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
