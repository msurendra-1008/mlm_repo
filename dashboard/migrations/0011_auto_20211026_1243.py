# Generated by Django 3.2.5 on 2021-10-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20211013_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmregistration',
            name='contact_person',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='firmregistration',
            name='contact_person_mobile',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
