# Generated by Django 3.2.5 on 2021-08-16 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upa', '0018_auto_20210816_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bussinesscardfees',
            old_name='general_bussiness_card',
            new_name='green_bussiness_card',
        ),
        migrations.RenameField(
            model_name='bussinesscardfees',
            old_name='pvc_bussiness_card',
            new_name='red_chip_bussiness_card',
        ),
        migrations.RenameField(
            model_name='bussinesscardfees',
            old_name='pvc_chip_bussiness_card',
            new_name='yellow_bussiness_card',
        ),
    ]
