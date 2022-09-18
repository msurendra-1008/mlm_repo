# Generated by Django 3.2.5 on 2021-08-31 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20210831_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='right_upa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_branch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='left_branch',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_branch',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='right_branch',
            field=models.BooleanField(default=False),
        ),
    ]