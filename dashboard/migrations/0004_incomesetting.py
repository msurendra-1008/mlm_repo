# Generated by Django 3.2.5 on 2021-10-04 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_upachangerequest_reply_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_side', models.IntegerField(blank=True, default=0, null=True)),
                ('middle_side', models.IntegerField(blank=True, default=0, null=True)),
                ('right_side', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income_setting', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income_setting_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
