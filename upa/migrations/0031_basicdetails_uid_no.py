# Generated by Django 3.2.5 on 2021-08-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upa', '0030_auto_20210827_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='uid_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='UID No.'),
        ),
    ]
