# Generated by Django 3.2.5 on 2021-08-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upa', '0022_servicerequired_account_passbook_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequired',
            name='e_account_statement_charge',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
