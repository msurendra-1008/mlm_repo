# Generated by Django 3.2.5 on 2021-09-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210831_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='initial_form_status',
            field=models.BooleanField(default=False),
        ),
    ]
