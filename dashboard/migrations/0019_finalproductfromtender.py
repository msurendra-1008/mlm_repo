# Generated by Django 3.2.5 on 2022-02-16 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_tenderproduct_tender_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalProductFromTender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('negotiated_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('tender_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.tenderraise')),
            ],
        ),
    ]
