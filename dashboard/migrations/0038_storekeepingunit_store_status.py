# Generated by Django 3.2.5 on 2022-03-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_auto_20220306_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='storekeepingunit',
            name='store_Status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('In Active', 'In Active'), ('Closed', 'Closed')], default='Active', max_length=10, null=True),
        ),
    ]
