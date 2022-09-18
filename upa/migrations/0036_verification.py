# Generated by Django 3.2.5 on 2021-09-03 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210831_1256'),
        ('upa', '0035_auto_20210902_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('applicant_image', models.ImageField(blank=True, null=True, upload_to='verification/applicant/images')),
                ('id_proof', models.ImageField(blank=True, null=True, upload_to='verification/applicant/id_proof')),
                ('verifier_id', models.IntegerField(blank=True, null=True)),
                ('verifier_image', models.ImageField(upload_to='verification/verifier/images')),
                ('verification_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verification', to='accounts.profile')),
            ],
        ),
    ]
