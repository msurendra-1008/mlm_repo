# Generated by Django 3.2.5 on 2023-04-16 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0048_alter_upachangerequest_form_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenderproduct',
            name='created_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]