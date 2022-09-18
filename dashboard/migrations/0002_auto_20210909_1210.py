# Generated by Django 3.2.5 on 2021-09-09 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210831_1256'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upachangerequest',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Read', 'Read')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='upachangerequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='changes_request', to='accounts.profile'),
        ),
    ]