# Generated by Django 3.2.5 on 2022-03-06 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_alter_recievedproducts_tender_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreLocationDefinition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locatio_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreKeepingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(blank=True, max_length=150, null=True)),
                ('store_address_one', models.CharField(blank=True, max_length=100, null=True)),
                ('store_address_two', models.CharField(blank=True, max_length=200, null=True)),
                ('store_address_three', models.CharField(blank=True, max_length=200, null=True)),
                ('store_size', models.CharField(blank=True, help_text='100 x 200', max_length=100, null=True)),
                ('no_of_racks', models.IntegerField(blank=True, default=0, null=True)),
                ('avg_section_rack', models.IntegerField(blank=True, default=1, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.storelocationdefinition')),
            ],
        ),
    ]