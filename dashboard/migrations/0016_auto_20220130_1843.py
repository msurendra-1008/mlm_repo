# Generated by Django 3.2.5 on 2022-01-30 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0015_bulkordertotenderfirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenderproduct',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_tender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tenderproduct',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_tender', to=settings.AUTH_USER_MODEL),
        ),
    ]
