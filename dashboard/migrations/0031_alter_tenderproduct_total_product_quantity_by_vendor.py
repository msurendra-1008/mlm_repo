# Generated by Django 3.2.5 on 2022-02-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_tenderproduct_total_product_quantity_by_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenderproduct',
            name='total_product_quantity_by_vendor',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
