# Generated by Django 3.2.5 on 2022-03-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_productinstore'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinstore',
            name='product_status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('In Active', 'In Active')], default='Active', max_length=10, null=True),
        ),
    ]
