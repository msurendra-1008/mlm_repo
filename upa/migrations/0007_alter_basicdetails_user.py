# Generated by Django 3.2.5 on 2021-07-29 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('upa', '0006_alter_basicdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
